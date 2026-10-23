import importlib.util
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

spec = importlib.util.spec_from_file_location('maintenance', Path(__file__).resolve().parents[1] / 'scripts/maintenance_orchestrator.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class MaintenanceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        config = {'routes': {}, 'overrides': {}}
        for cluster, workflow in [('guides', 'guide'), ('marques', 'brand')]:
            config['routes'][cluster] = {'workflow': workflow, 'cadence_days': 30, 'validator': 'check.py'}
            for mode in ('analysis', 'content'):
                p = self.root / f'.agents/skills/{workflow}-{mode}-workflow/SKILL.md'
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text('existing skill')
            for slug in ['a', 'nested/b']:
                p = self.root / cluster / slug / 'index.html'
                p.parent.mkdir(parents=True)
                p.write_text('content')
        m.write(self.root / 'maintenance.config.json', config)
        m.write(self.root / '.content/maintenance/index.json', {'pages': {}})

    def test_routing_nested_pages_and_fairness(self):
        plan = m.prepare(self.root, date.today(), 2)
        self.assertEqual(plan['inventory_count'], 4)
        self.assertEqual({p['workflow'] for p in plan['pages']}, {'guide', 'brand'})
        plan = m.prepare(self.root, date.today(), 10, ['/marques/nested/b/'])
        self.assertIn('brand-analysis', plan['pages'][0]['analysis_workflow'])
        self.assertEqual(m.read(self.root / '.content/maintenance/index.json')['pages'], {})

    def result(self, plan):
        p = self.root / '.content/reviews/a.md'
        p.parent.mkdir(parents=True)
        p.write_text('AUDIT KEEP with sources')
        return {'pages': [{'url': plan['pages'][0]['url'], 'reviewed_at': date.today().isoformat(),
                           'decision': 'KEEP', 'audit_report': '.content/reviews/a.md'}]}

    def test_record_cadence_and_changed_page(self):
        plan = m.prepare(self.root, date.today(), 1)
        m.record(self.root, plan, self.result(plan))
        later = m.prepare(self.root, date.today(), 10)
        self.assertNotIn(plan['pages'][0]['url'], [p['url'] for p in later['pages']])
        (self.root / plan['pages'][0]['file']).write_text('changed')
        later = m.prepare(self.root, date.today(), 10)
        self.assertIn('changed_since_audit', [p['reason'] for p in later['pages']])

    def test_reject_stale_plan_without_state_write(self):
        plan = m.prepare(self.root, date.today(), 1)
        results = self.result(plan)
        (self.root / plan['pages'][0]['file']).write_text('changed')
        with self.assertRaises(ValueError):
            m.record(self.root, plan, results)
        self.assertEqual(m.read(self.root / '.content/maintenance/index.json')['pages'], {})

    def test_unknown_url_and_missing_skill_fail(self):
        with self.assertRaises(ValueError):
            m.prepare(self.root, date.today(), 1, ['/unknown/'])
        (self.root / '.agents/skills/guide-analysis-workflow/SKILL.md').unlink()
        with self.assertRaises(ValueError):
            m.prepare(self.root, date.today(), 1)


if __name__ == '__main__':
    unittest.main()

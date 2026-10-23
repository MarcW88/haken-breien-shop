import { chromium } from '@playwright/test';
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
const slug = (process.env.HAKEN_PAGE || '').trim().replace(/^\/+|\/+$/g, '');
if (slug.includes('/') || slug === '..') throw Error('Expected one page slug');
const pages = slug ? ['/haken/' + (slug === 'haken' ? '' : slug + '/')] : ['/','/haken/','/haken/voor-beginners/','/haken/steken/','/haken/technieken/','/haken/projecten/'];
const output = '.artifacts/haken/screenshots';
fs.mkdirSync(output,{recursive:true});
const server=spawn('python3',['-m','http.server','8765','--bind','127.0.0.1'],{stdio:'ignore'});
const browser=await chromium.launch({headless:true});
try {
  await new Promise(r=>setTimeout(r,1500));
  for(const width of [390,1440]){
    const page=await browser.newPage({viewport:{width,height:850},deviceScaleFactor:1});
    for(const route of pages){
      const response=await page.goto('http://127.0.0.1:8765'+route,{waitUntil:'networkidle'});
      if(!response?.ok())throw Error(route+' returned '+response?.status());
      const bad=await page.evaluate(()=>document.documentElement.scrollWidth > window.innerWidth+2);
      if(bad)throw Error(route+' has horizontal overflow at '+width);
      const title=await page.title();
      if(!title)throw Error(route+' missing title');
      await page.screenshot({path:path.join(output,route.split('/').filter(Boolean).join('-')+'-'+width+'.png'),fullPage:true});
    }
    await page.close();
  }
} finally {await browser.close();server.kill();}
console.log('Visual smoke test passed: '+pages.length+' pages at desktop and mobile widths.');

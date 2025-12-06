;(function(){
  function pathToAssets(){var p=location.pathname;return p.indexOf('/lesson-plans/')>-1||p.indexOf('/notebook-sessions/')>-1?'../assets':'assets'}
  function setFavicon(){var href=pathToAssets()+"/brands/favicon-straydog.png";var l=document.querySelector('link[rel="icon"]');if(!l){l=document.createElement('link');l.setAttribute('rel','icon');l.setAttribute('type','image/png');document.head.appendChild(l)}l.setAttribute('href',href)}
  function injectFooter(){var footer=document.createElement('div');footer.className='sd-footer';footer.innerHTML=
    '<img class="sd-footer-gear" src="'+pathToAssets()+'/brands/stray-gear.png" alt="StrayDog" aria-hidden="true">'
    +'<div class="sd-credits">Enhanced curriculum for the Returned Citizen community by <a href="https://www.straydog-syndications-llc.com/" target="_blank" rel="noopener">StrayDog Syndications LLC</a></div>'
    +'<div class="sd-links" aria-label="Creator GitHub links">'
    +  '<a href="https://github.com/StrayDogSyn" target="_blank" aria-label="StrayDogSyn GitHub">'
    +    '<svg class="sd-github" viewBox="0 0 16 16" role="img" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.01.08-2.1 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.09.16 1.9.08 2.1.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>'
    +  '</a>'
    +  '<a href="https://github.com/miasmith81" target="_blank" aria-label="miasmith81 GitHub">'
    +    '<svg class="sd-github" viewBox="0 0 16 16" role="img" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.01.08-2.1 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.09.16 1.9.08 2.1.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>'
    +  '</a>'
    +'</div>'
  ;
  var host=document.querySelector('footer');if(host){host.appendChild(footer)}else{document.body.appendChild(footer)}
  }
  function applyWatermarkIfEligible(){var p=location.pathname;var eligible=p.endsWith('/index.html')||p.endsWith('/community-partners.html')||p==='/';if(eligible){document.body.classList.add('sd-watermark')}}
  function abAssign(){var urlParam=new URLSearchParams(location.search).get('variant');var v=localStorage.getItem('sd-ab-variant');if(urlParam==='A'||urlParam==='B'){v=urlParam}else if(!v){v=Math.random()<0.5?'A':'B'}localStorage.setItem('sd-ab-variant',v);return v}
  function abMetricsInit(){var v=abAssign();var key='sd-ab-metrics';var m=localStorage.getItem(key);var metrics=m?JSON.parse(m):{variant:v,clicks:0,notebookClicks:0,completeClicks:0,scrollMax:0};function save(){localStorage.setItem(key,JSON.stringify(metrics))}
    document.addEventListener('click',function(e){var t=e.target;if(t.matches('.action-btn.primary')){metrics.clicks++}if(t.matches('.notebook-btn')){metrics.notebookClicks++}if(t.matches('.complete-btn')){metrics.completeClicks++}save()});
    document.addEventListener('scroll',function(){var h=document.documentElement;var s=(h.scrollTop||document.body.scrollTop);var d=(h.scrollHeight-h.clientHeight);var p=d?Math.min(100,Math.max(0,(s/d)*100)):0;if(p>metrics.scrollMax){metrics.scrollMax=p;save()}});
    if(v==='B'){document.documentElement.setAttribute('data-branding','minimal')}
  }
  function init(){setFavicon();applyWatermarkIfEligible();injectFooter();abMetricsInit()}
  document.addEventListener('DOMContentLoaded',init)
})();


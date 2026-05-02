// ── SCROLL REVEAL ──
function initReveal(){
  const els=document.querySelectorAll('.reveal,.reveal-l,.reveal-r');
  const io=new IntersectionObserver(entries=>{
    entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}});
  },{threshold:0.1});
  els.forEach(el=>io.observe(el));
}

// ── COUNTER ──
function animateCounter(el){
  const target=parseInt(el.dataset.target);
  let cur=0;const step=Math.ceil(target/55);
  const t=setInterval(()=>{cur=Math.min(cur+step,target);el.textContent=cur;if(cur>=target)clearInterval(t);},20);
}
function initCounters(){
  const els=document.querySelectorAll('.counter');
  const io=new IntersectionObserver(entries=>{
    entries.forEach(e=>{if(e.isIntersecting){animateCounter(e.target);io.unobserve(e.target)}});
  },{threshold:0.5});
  els.forEach(el=>io.observe(el));
}

// ── FAQ ──
function initFaq(){
  document.querySelectorAll('.faq-q').forEach(btn=>{
    btn.addEventListener('click',()=>{
      const item=btn.closest('.faq-item');
      const open=item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(i=>i.classList.remove('open'));
      if(!open)item.classList.add('open');
    });
  });
}

// ── FORM SUBMIT ──
function initForm(){
  document.querySelectorAll('.btn-submit').forEach(btn=>{
    btn.addEventListener('click',()=>{
      const orig=btn.innerHTML;
      btn.innerHTML='✓ Sent! We\'ll contact you shortly';
      btn.style.background='#16a34a';
      setTimeout(()=>{btn.innerHTML=orig;btn.style.background='';},3000);
    });
  });
}

// ── FLOAT WA ──
function initFloatWa(){
  const lbl=document.getElementById('waLabel');
  if(!lbl)return;
  document.getElementById('waClose')?.addEventListener('click',e=>{e.stopPropagation();lbl.classList.add('gone');});
  setTimeout(()=>lbl.classList.add('gone'),8000);
}

// ── NAV ACTIVE ──
function initNav(){
  const path=location.pathname.split('/').pop()||'index.html';
  document.querySelectorAll('.nav-link,.dd-item').forEach(a=>{
    const href=a.getAttribute('href')||'';
    if(href&&(href===path||href.endsWith('/'+path))){
      a.classList.add('active');
      const dd=a.closest('.dropdown');
      if(dd)dd.querySelector('.nav-link')?.classList.add('active');
    }
  });
}

// ── CONTACT FORM ──
function initContactForm(){
  const form=document.getElementById('contactForm');
  if(!form)return;
  form.addEventListener('submit',e=>{
    e.preventDefault();
    const btn=form.querySelector('button[type=submit]');
    btn.textContent='✓ Message Sent!';btn.style.background='#16a34a';
    setTimeout(()=>{btn.textContent='Send Message';btn.style.background='';},3000);
  });
}

document.addEventListener('DOMContentLoaded',()=>{
  initReveal();initCounters();initFaq();initForm();initFloatWa();initNav();initContactForm();
});

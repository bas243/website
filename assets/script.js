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
const WEB3FORMS_URL = 'https://api.web3forms.com/submit';
const WEB3FORMS_KEY = '2c713ffc-e405-4846-a8c0-f32ea78cef4a';

function handleSubmit(btn){
  const form = btn.closest('.quote-card') || btn.closest('.contact-form');
  const agreeRow = form ? form.querySelector('.agree-row') : null;
  const checkbox = agreeRow ? agreeRow.querySelector('input[type="checkbox"]') : null;

  // Validate T&C checkbox
  if (checkbox && !checkbox.checked) {
    agreeRow.classList.remove('error');
    void agreeRow.offsetWidth;
    agreeRow.classList.add('error');
    checkbox.focus();
    return;
  }
  if (agreeRow) agreeRow.classList.remove('error');

  // Collect all field values
  const data = {};
  if (form) {
    // Text/email/tel/date inputs
    form.querySelectorAll('input[type="text"],input[type="email"],input[type="tel"],input[type="date"]').forEach((el, i) => {
      const label = form.querySelectorAll('label')[i] ? form.querySelectorAll('label')[i].textContent.trim().replace(/\s*\*$/,'') : ('Field '+(i+1));
      if (el.value.trim()) data[label] = el.value.trim();
    });
    // Selects (country code + service type)
    const selects = form.querySelectorAll('select');
    selects.forEach((sel, i) => {
      const val = sel.options[sel.selectedIndex]?.text || sel.value;
      if (val && val !== '— Select Service —') {
        data[i === 0 && selects.length > 1 ? 'Country Code' : 'Service Type'] = val;
      }
    });
    // Textarea
    const ta = form.querySelector('textarea');
    if (ta && ta.value.trim()) data['Additional Requirements'] = ta.value.trim();
    // Page source
    data['Page'] = document.title || window.location.pathname;
  }

  // Loading state
  const orig = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = '⏳ Sending…';

  fetch(WEB3FORMS_URL, {
    method: 'POST',
    headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
    body: JSON.stringify({
      access_key: WEB3FORMS_KEY,
      subject: '📩 New Quote Request — AssessmentHelp',
      from_name: 'AssessmentHelp Website',
      ...data
    })
  })
  .then(res => res.json())
  .then(json => {
    if (json.success) {
      btn.innerHTML = '✅ Sent! We\'ll contact you shortly';
      btn.style.background = '#16a34a';
      if (form) {
        form.querySelectorAll('input[type="text"],input[type="email"],input[type="tel"],input[type="date"],textarea').forEach(el => el.value = '');
        if (checkbox) checkbox.checked = false;
      }
      setTimeout(() => { btn.innerHTML = orig; btn.style.background = ''; btn.disabled = false; }, 4000);
    } else {
      btn.innerHTML = '❌ Error — please try WhatsApp';
      btn.style.background = '#dc2626';
      setTimeout(() => { btn.innerHTML = orig; btn.style.background = ''; btn.disabled = false; }, 4000);
    }
  })
  .catch(() => {
    btn.innerHTML = '❌ Network error — please try WhatsApp';
    btn.style.background = '#dc2626';
    setTimeout(() => { btn.innerHTML = orig; btn.style.background = ''; btn.disabled = false; }, 4000);
  });
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

const WA_NUMBER = 'https://wa.me/919876543210';

// detect depth: services/ and subjects/ are one level deep
const isRoot = !(location.pathname.includes('/services/') || location.pathname.includes('/subjects/'));
const pre = isRoot ? '' : '../';

function navHTML(){
  return `
<header>
  <div class="nav-wrap">
    <a href="${pre}index.html" class="logo">
      <div class="logo-box">A</div>
      <div>ASSESSMENT<br><small>Powered By The Student Helpline</small></div>
    </a>
    <nav>
      <a class="nav-link" href="${pre}index.html">Home</a>
      <div class="dropdown">
        <span class="nav-link">Services
          <svg viewBox="0 0 20 20" fill="currentColor"><path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"/></svg>
        </span>
        <div class="dropdown-menu">
          <a class="dd-item" href="${pre}services/assessment-help.html">Assessment Help</a>
          <a class="dd-item" href="${pre}services/assignment-help.html">Assignment Help</a>
          <a class="dd-item" href="${pre}services/coursework-help.html">Coursework Help</a>
          <a class="dd-item" href="${pre}services/essay-writing.html">Essay Writing Help</a>
          <a class="dd-item" href="${pre}services/dissertation-help.html">Dissertation Help</a>
          <a class="dd-item" href="${pre}services/case-study.html">Case Study Help</a>
          <a class="dd-item" href="${pre}services/online-exam.html">Online Exam Help</a>
        </div>
      </div>
      <div class="dropdown">
        <span class="nav-link">Subjects
          <svg viewBox="0 0 20 20" fill="currentColor"><path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"/></svg>
        </span>
        <div class="dropdown-menu">
          <a class="dd-item" href="${pre}subjects/management.html">Management</a>
          <a class="dd-item" href="${pre}subjects/law.html">Law</a>
          <a class="dd-item" href="${pre}subjects/nursing.html">Nursing</a>
          <a class="dd-item" href="${pre}subjects/engineering.html">Engineering</a>
          <a class="dd-item" href="${pre}subjects/accounting.html">Accounting</a>
          <a class="dd-item" href="${pre}subjects/it-computer-science.html">IT & Computer Science</a>
          <a class="dd-item" href="${pre}subjects/finance-economics.html">Finance & Economics</a>
        </div>
      </div>
      <a class="nav-link" href="${pre}about.html">About Us</a>
      <a class="nav-link" href="${pre}how-it-works.html">How It Works</a>
      <a class="nav-link" href="${pre}contact.html">Contact</a>
    </nav>
    <div class="nav-right">
      <a href="${WA_NUMBER}" target="_blank" class="btn-wa">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="#25D366"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        WhatsApp
      </a>
      <button class="btn-quote" onclick="window.location='${pre}contact.html'">Get Free Quote</button>
    </div>
  </div>
</header>`;
}

function footerHTML(){
  return `
<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div>
        <div class="footer-logo"><div class="logo-box">A</div><div>ASSESSMENT<br><small style="font-size:.5rem;opacity:.5;font-weight:400">Powered by The Student Helpline</small></div></div>
        <p class="footer-tagline">Your trusted partner for professional academic assessment help. We help students achieve academic excellence worldwide.</p>
        <div class="social-row"><div class="sicon">f</div><div class="sicon">𝕏</div><div class="sicon">in</div><div class="sicon">ig</div></div>
      </div>
      <div class="footer-col"><h4>Our Services</h4><ul>
        <li><a href="${pre}services/assessment-help.html">Assessment Help</a></li>
        <li><a href="${pre}services/assignment-help.html">Assignment Help</a></li>
        <li><a href="${pre}services/coursework-help.html">Coursework Help</a></li>
        <li><a href="${pre}services/essay-writing.html">Essay Writing Help</a></li>
        <li><a href="${pre}services/dissertation-help.html">Dissertation Help</a></li>
        <li><a href="${pre}services/case-study.html">Case Study Help</a></li>
        <li><a href="${pre}services/online-exam.html">Online Exam Help</a></li>
      </ul></div>
      <div class="footer-col"><h4>Subjects</h4><ul>
        <li><a href="${pre}subjects/management.html">Management</a></li>
        <li><a href="${pre}subjects/law.html">Law</a></li>
        <li><a href="${pre}subjects/nursing.html">Nursing</a></li>
        <li><a href="${pre}subjects/engineering.html">Engineering</a></li>
        <li><a href="${pre}subjects/accounting.html">Accounting</a></li>
        <li><a href="${pre}subjects/it-computer-science.html">IT & Computer Science</a></li>
        <li><a href="${pre}subjects/finance-economics.html">Finance & Economics</a></li>
      </ul></div>
      <div class="footer-col"><h4>Quick Links</h4><ul>
        <li><a href="${pre}about.html">About Us</a></li>
        <li><a href="${pre}how-it-works.html">How It Works</a></li>
        <li><a href="${pre}contact.html">Contact Us</a></li>
        <li><a href="${pre}contact.html">Privacy Policy</a></li>
        <li><a href="${pre}contact.html">Terms of Service</a></li>
        <li><a href="${pre}contact.html">Refund Policy</a></li>
      </ul></div>
      <div class="footer-col"><h4>Contact Us</h4>
        <div class="fc-item"><span class="fc-icon">✉</span><span>help@assessmenthelp.io</span></div>
        <div class="fc-item"><span class="fc-icon">📞</span><span>+91 98765 43210<br>+44 791 802 3966</span></div>
        <div class="fc-item"><span class="fc-icon">🕐</span><span>24/7 Support Available</span></div>
        <button class="fwa" onclick="window.open('${WA_NUMBER}','_blank')">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#fff"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
          Chat on WhatsApp
        </button>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 AssessmentHelp.io. All rights reserved.</p>
      <div class="footer-trust-row"><span class="ftr">100% Secure Payment</span><span class="ftr">All Major Cards Accepted</span><span class="ftr">SSL Encrypted</span></div>
      <p>Disclaimer: Services provided are for reference and research purposes only.</p>
    </div>
  </div>
</footer>
<div class="float-wa">
  <button class="float-btn" onclick="window.open('${WA_NUMBER}','_blank')">
    <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  </button>
  <div class="float-label" id="waLabel"><span>Chat with Us</span><span class="flx" onclick="closeWa(event)">✕</span></div>
</div>`;
}

document.addEventListener('DOMContentLoaded', () => {
  document.body.insertAdjacentHTML('afterbegin', navHTML());
  document.body.insertAdjacentHTML('beforeend', footerHTML());
  // highlight active nav link
  document.querySelectorAll('a.dd-item, a.nav-link').forEach(a => {
    const href = a.getAttribute('href');
    if(href && location.pathname.endsWith(href.replace(/^.*\//,''))) {
      a.classList.add('active');
    }
  });
});

#!/usr/bin/env python3
"""Generate all pages for the AssessmentHelp website."""

import os

BASE = "/home/claude/website"
WA = "https://wa.me/your-number"

# ── shared snippets ──────────────────────────────────────────────

def nav(depth=0):
    prefix = "../" * depth
    return f"""<header>
  <div class="nav-wrap">
    <a href="{prefix}index.html" class="logo">
      <div class="logo-box">A</div>
      <div>ASSESSMENT<br><small>Powered By The Student Helpline</small></div>
    </a>
    <nav>
      <a class="nav-link" href="{prefix}index.html">Home</a>
      <div class="dropdown">
        <span class="nav-link">Services
          <svg viewBox="0 0 20 20" fill="currentColor"><path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"/></svg>
        </span>
        <div class="dropdown-menu">
          <a class="dd-item" href="{prefix}services/assessment-help.html">Assessment Help</a>
          <a class="dd-item" href="{prefix}services/assignment-help.html">Assignment Help</a>
          <a class="dd-item" href="{prefix}services/coursework-help.html">Coursework Help</a>
          <a class="dd-item" href="{prefix}services/essay-writing-help.html">Essay Writing Help</a>
          <a class="dd-item" href="{prefix}services/dissertation-help.html">Dissertation Help</a>
          <a class="dd-item" href="{prefix}services/case-study-help.html">Case Study Help</a>
          <a class="dd-item" href="{prefix}services/online-exam-help.html">Online Exam Help</a>
        </div>
      </div>
      <div class="dropdown">
        <span class="nav-link">Subjects
          <svg viewBox="0 0 20 20" fill="currentColor"><path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"/></svg>
        </span>
        <div class="dropdown-menu">
          <a class="dd-item" href="{prefix}subjects/management.html">Management</a>
          <a class="dd-item" href="{prefix}subjects/law.html">Law</a>
          <a class="dd-item" href="{prefix}subjects/nursing.html">Nursing</a>
          <a class="dd-item" href="{prefix}subjects/engineering.html">Engineering</a>
          <a class="dd-item" href="{prefix}subjects/accounting.html">Accounting</a>
          <a class="dd-item" href="{prefix}subjects/it-computer-science.html">IT & Computer Science</a>
          <a class="dd-item" href="{prefix}subjects/finance-economics.html">Finance & Economics</a>
        </div>
      </div>
      <a class="nav-link" href="{prefix}about.html">About Us</a>
      <a class="nav-link" href="{prefix}how-it-works.html">How It Works</a>
      <a class="dd-item" href="{prefix}contact.html" style="padding:8px 11px;border-radius:6px;font-size:.86rem;font-weight:500;color:#2D3748;display:inline-block;transition:color .15s,background .15s">Contact</a>
    </nav>
    <div class="nav-right">
      <a href="{WA}" class="btn-wa" target="_blank">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="#25D366"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        WhatsApp
      </a>
      <button class="btn-quote" onclick="location.href='{prefix}contact.html'">Get Free Quote</button>
    </div>
  </div>
</header>"""

def ticker():
    items = ["🎉 20% OFF for New Customers","📚 1500+ Expert Writers Available","⚡ 3-Hour Urgent Delivery","✅ 100% Plagiarism-Free Guarantee","🔒 100% Confidential","💳 Pay After Delivery Option"]
    doubled = items * 2
    html = "".join(f'<span class="tick-item">{i}</span>' for i in doubled)
    return f'<div class="ticker-wrap"><div class="ticker">{html}</div></div>'

def quote_card(depth=0):
    prefix = "../" * depth
    return f"""<div class="quote-card reveal-r">
  <div class="qcard-head">Get Free Quote Instantly<small>Enter your details and get a free quote instantly</small></div>
  <div class="form-group"><label>Your Name</label><input type="text" placeholder="Your Name"></div>
  <div class="form-group"><label>Phone Number</label>
    <div class="form-row">
      <select><option>IN +91</option><option>UK +44</option><option>AU +61</option><option>US +1</option></select>
      <input type="tel" placeholder="Phone Number">
    </div>
  </div>
  <div class="form-group"><label>Email Address</label><input type="email" placeholder="your@email.com"></div>
  <div class="form-group"><label>Type of Service</label>
    <select><option>Assessment Help</option><option>Assignment Help</option><option>Coursework Help</option><option>Dissertation Help</option></select>
  </div>
  <button class="btn-submit">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 2L11 13M22 2L15 22l-4-9-9-4 20-7z"/></svg>
    Get Free Quote →
  </button>
  <div class="form-trust"><span>Free consultation</span><span>No obligation</span><span>Instant response</span></div>
  <div class="card-stats">
    <div><div class="cstat-num"><span class="counter" data-target="180">0</span>K+</div><div class="cstat-label">Papers Done</div></div>
    <div><div class="cstat-num"><span class="counter" data-target="99">0</span>%</div><div class="cstat-label">Satisfaction</div></div>
    <div><div class="cstat-num">24/7</div><div class="cstat-label">Support</div></div>
  </div>
</div>"""

def float_wa():
    return f"""<div class="float-wa">
  <a href="{WA}" target="_blank"><button class="float-btn"><svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></button></a>
  <div class="float-label" id="waLabel">
    <span>Chat with Us</span><span class="flx" id="waClose">✕</span>
  </div>
</div>"""

def footer(depth=0):
    p = "../" * depth
    return f"""<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div>
        <div class="footer-logo"><div class="logo-box">A</div><div>ASSESSMENT<br><small style="font-size:.5rem;opacity:.4;font-weight:400">Powered by The Student Helpline</small></div></div>
        <p class="footer-tagline">Your trusted partner for professional academic assessment help. We help students achieve excellence worldwide.</p>
        <div class="social-row">
          <div class="sicon">f</div><div class="sicon">𝕏</div><div class="sicon">in</div><div class="sicon">ig</div>
        </div>
      </div>
      <div class="footer-col"><h4>Our Services</h4><ul>
        <li><a href="{p}services/assessment-help.html">Assessment Help</a></li>
        <li><a href="{p}services/assignment-help.html">Assignment Help</a></li>
        <li><a href="{p}services/coursework-help.html">Coursework Help</a></li>
        <li><a href="{p}services/essay-writing-help.html">Essay Writing Help</a></li>
        <li><a href="{p}services/dissertation-help.html">Dissertation Help</a></li>
        <li><a href="{p}services/case-study-help.html">Case Study Help</a></li>
        <li><a href="{p}services/online-exam-help.html">Online Exam Help</a></li>
      </ul></div>
      <div class="footer-col"><h4>Subjects</h4><ul>
        <li><a href="{p}subjects/management.html">Management</a></li>
        <li><a href="{p}subjects/law.html">Law</a></li>
        <li><a href="{p}subjects/nursing.html">Nursing</a></li>
        <li><a href="{p}subjects/engineering.html">Engineering</a></li>
        <li><a href="{p}subjects/accounting.html">Accounting</a></li>
        <li><a href="{p}subjects/it-computer-science.html">IT &amp; Computer Science</a></li>
        <li><a href="{p}subjects/finance-economics.html">Finance &amp; Economics</a></li>
      </ul></div>
      <div class="footer-col"><h4>Quick Links</h4><ul>
        <li><a href="{p}about.html">About Us</a></li>
        <li><a href="{p}how-it-works.html">How It Works</a></li>
        <li><a href="{p}contact.html">Contact Us</a></li>
        <li><a href="{p}contact.html">Privacy Policy</a></li>
        <li><a href="{p}contact.html">Terms of Service</a></li>
        <li><a href="{p}contact.html">Refund Policy</a></li>
      </ul></div>
      <div class="footer-col"><h4>Contact Us</h4>
        <div class="fc-item"><span class="fc-icon">✉</span><span>help@assessmenthelp.io</span></div>
        <div class="fc-item"><span class="fc-icon">📞</span><span>+91 98765 43210<br>+44 791 802 3966</span></div>
        <div class="fc-item"><span class="fc-icon">🕐</span><span>24/7 Support Available</span></div>
        <a href="{WA}" target="_blank"><button class="fwa">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#fff"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
          Chat on WhatsApp
        </button></a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 AssessmentHelp.io. All rights reserved.</p>
      <div class="footer-trust-row">
        <span class="ftr">100% Secure Payment</span>
        <span class="ftr">All Major Cards Accepted</span>
        <span class="ftr">SSL Encrypted</span>
      </div>
      <p>Disclaimer: Services are for reference and research purposes only.</p>
    </div>
  </div>
</footer>"""

def faq_section(items, depth=0):
    html = '<section id="faq"><div class="container"><div class="section-head reveal"><h2>Frequently Asked <span>Questions</span></h2><p>Everything you need to know</p></div><div class="faq-list reveal">'
    for q, a in items:
        html += f'<div class="faq-item"><div class="faq-q">{q}<div class="faq-icon">+</div></div><div class="faq-a"><div class="faq-a-inner">{a}</div></div></div>'
    html += '</div></div></section>'
    return html

def benefits_section(items, title):
    html = f'<section class="service-benefits"><div class="container"><div class="section-head reveal"><h2>{title}</h2></div><div class="sb-grid">'
    for icon, h, p in items:
        html += f'<div class="sb-card reveal"><div class="sb-icon">{icon}</div><h3>{h}</h3><p>{p}</p></div>'
    html += '</div></div></section>'
    return html

def blue_band(h2, p_text, depth=0):
    prefix = "../" * depth
    return f"""<div class="blue-band">
  <div class="container">
    <h2>{h2}</h2>
    <p>{p_text}</p>
    <div class="band-btns">
      <button class="btn-white" onclick="location.href='{prefix}contact.html'">Get Free Quote →</button>
      <a href="{WA}" target="_blank"><button class="btn-ghost">Chat on WhatsApp</button></a>
    </div>
  </div>
</div>"""

def page(title, css_depth, body):
    p = "../" * css_depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — AssessmentHelp</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
{nav(css_depth)}
{body}
{float_wa()}
<script src="{p}assets/main.js"></script>
</body>
</html>"""

# ── HOME PAGE ──────────────────────────────────────────────────────────────────
home_body = f"""
<div class="home-hero">
  <div class="home-hero-inner">
    <div class="reveal-l">
      <h1 class="hero-h1"><span>Expert Assessment Help</span> for Students Worldwide: Top Assessment Helper Online</h1>
      <p class="hero-sub">Professional assessment writing assistance from 1500+ PhD-qualified experts. 100% original, AI-free content delivered on time.</p>
      <div class="ratings">
        <div class="rating-item"><span class="stars">★★★★★</span><span class="rating-text">4.9/5</span><span class="rating-src">Sitejabber</span></div>
        <div class="rating-item"><span class="stars">★★★★☆</span><span class="rating-text">4.7/5</span><span class="rating-src">Reviews.io</span></div>
      </div>
      <div class="trust-badges">
        <div class="badge">🛡️ 100% AI-Free</div>
        <div class="badge">⏰ On-Time</div>
        <div class="badge">👥 1500+ Experts</div>
      </div>
    </div>
    {quote_card(0)}
  </div>
</div>
{ticker()}
<section>
  <div class="container">
    <div class="feature-split">
      <div class="feature-visual reveal-l">
        <div class="fv-outer"><div class="fv-inner">🛡️</div><div class="fv-badge">100% Human Written</div></div>
      </div>
      <div class="feature-text reveal-r">
        <h2>Our Experts Don't Use <span>AI Tools</span></h2>
        <p>Unlike other services, we guarantee 100% human-written content. Every assessment is crafted by qualified experts with real academic experience.</p>
        <div class="check-grid">
          <div class="check-item">We follow your exact instructions</div>
          <div class="check-item">Pay after delivery option</div>
          <div class="check-item">We meet even tight deadlines</div>
          <div class="check-item">100% confidentiality ensured</div>
          <div class="check-item">Plagiarism &amp; AI-free work</div>
          <div class="check-item">24/7 support available</div>
        </div>
        <a href="{WA}" target="_blank"><button class="btn-blue">💬 Let's Chat</button></a>
      </div>
    </div>
  </div>
</section>
<section style="background:#F8FAFF" id="process">
  <div class="container">
    <div class="section-head reveal"><h2>How It <span>Works</span></h2><p>Three simple steps to get your assessment done by experts</p></div>
    <div class="process-row reveal">
      <div class="process-card"><div class="proc-icon">💬</div><h3>Share Your Assessment Details</h3><p>Connect via WhatsApp, email, or our form. Share deadline, word count, citation style and requirements.</p></div>
      <div class="proc-arrow">›</div>
      <div class="process-card"><div class="proc-icon">👨‍💼</div><h3>Get Free Pre-Assessment Consultation</h3><p>We connect you with a subject expert to discuss scope, approach, and brainstorm ideas for clarity.</p></div>
      <div class="proc-arrow">›</div>
      <div class="process-card"><div class="proc-icon">💳</div><h3>Get Quote &amp; Make Secure Payment</h3><p>We share a personalized quote. Negotiate pricing and make a secure payment to start immediately.</p></div>
    </div>
  </div>
</section>
{blue_band("Can I Pay Someone To Write My Assessment For Me?", "Need help with assessments? Help is on its way! We have a dedicated team of expert writers, support staff and quality check professionals working 24/7 to help you succeed.", 0)}
<section id="pricing">
  <div class="container">
    <div class="section-head reveal"><h2>Transparent <span>Pricing</span></h2><p>See exactly what's included in every order</p></div>
    <div class="pricing-grid reveal">
      <div class="pricing-card featured">
        <h3><span>Included in Price</span></h3>
        <div class="price-row"><span class="pl">Title Page &amp; Cover</span><span class="pv">FREE</span></div>
        <div class="price-row"><span class="pl">Table of Contents</span><span class="pv">FREE</span></div>
        <div class="price-row"><span class="pl">Reference / Bibliography</span><span class="pv">FREE</span></div>
        <div class="price-row"><span class="pl">Formatting (APA, Harvard, etc.)</span><span class="pv">FREE</span></div>
        <div class="price-row"><span class="pl">Unlimited Revisions</span><span class="pv">FREE</span></div>
        <div class="price-row"><span class="pl">Plagiarism Report</span><span class="pv">FREE</span></div>
        <div class="price-row"><span class="pl">Topic Consultation</span><span class="pv">FREE</span></div>
        <div class="price-row"><span class="pl">24/7 Support</span><span class="pv">FREE</span></div>
      </div>
      <div class="pricing-card">
        <h3>Premium Add-ons</h3>
        <div class="addon-row"><span class="al">VIP Support</span><span class="ap">$9.99</span></div>
        <div class="addon-row"><span class="al">Extended Revision Period</span><span class="ap">$4.99</span></div>
        <div class="addon-row"><span class="al">Top Writer Upgrade</span><span class="ap">$14.99</span></div>
        <div class="addon-row"><span class="al">Copy of Sources</span><span class="ap">$9.99</span></div>
        <div class="pricing-from"><small>Starting from</small><div><span class="pricing-price">$9.99</span><span style="color:var(--muted);font-size:.85rem">/page</span></div></div>
      </div>
    </div>
    <div class="pricing-cta-wrap reveal"><p>Not sure? Try our service with a 1-page trial</p><button class="btn-blue" onclick="location.href='contact.html'">Get Started →</button></div>
  </div>
</section>
<section style="background:#F8FAFF">
  <div class="container">
    <div class="section-head reveal"><h2>Benefits of Our <span>Assessment Help</span></h2></div>
    <div class="benefits-grid">
      <div class="benefit-card reveal"><div class="ben-icon">✍️</div><h3>Expert Writers</h3><p>1500+ PhD-certified writers with expertise across 120+ subjects and years of academic experience.</p></div>
      <div class="benefit-card reveal" style="transition-delay:.07s"><div class="ben-icon">📄</div><h3>Original Content</h3><p>Every assessment written from scratch, ensuring 100% originality with a free plagiarism report.</p></div>
      <div class="benefit-card reveal" style="transition-delay:.14s"><div class="ben-icon">⚡</div><h3>Fast Turnaround</h3><p>Need it urgently? We deliver quality work in as little as 3 hours without compromising quality.</p></div>
      <div class="benefit-card reveal" style="transition-delay:.21s"><div class="ben-icon">💰</div><h3>Money-Back Guarantee</h3><p>Not satisfied? Get a full refund with our money-back assurance — no questions asked.</p></div>
    </div>
  </div>
</section>
{faq_section([
  ("How do I place an order for assessment help?","Simply contact us via WhatsApp, email, or fill out our form. Share your assessment details, deadline, and requirements. Our team will connect you with a suitable expert and provide a free quote within minutes."),
  ("Can you handle urgent assessment orders?","Yes! We specialize in urgent deliveries. Our experts can complete assessments in as little as 3 hours for smaller tasks. For larger projects, we'll give you a realistic timeline."),
  ("Is your assessment help confidential?","Absolutely. Your personal details, order information, and communication are 100% confidential and never shared with third parties. We use encrypted connections for all data."),
  ("What is your revision policy?","We offer unlimited free revisions until you're completely satisfied. Simply share your feedback and our expert will make the necessary changes immediately."),
  ("Do you provide a plagiarism report?","Yes, every order comes with a free plagiarism report. All our work is 100% original, written from scratch. We never use AI tools or recycled content."),
])}
{footer(0)}
"""

with open(f"{BASE}/index.html", "w") as f:
    f.write(page("Expert Assessment Help for Students Worldwide", 0, home_body))

# ── ABOUT PAGE ──────────────────────────────────────────────────────────────────
about_body = f"""
<div class="page-hero">
  <h1>About Us</h1>
  <p>Your trusted partner for professional academic assessment help since 2015</p>
</div>
<section>
  <div class="container">
    <div class="about-grid">
      <div class="about-img-placeholder reveal-l">🎓</div>
      <div class="about-text reveal-r">
        <h2>Who <span>We Are</span></h2>
        <p>AssessmentHelp is a professional academic support service powered by The Student Helpline. We have helped over 180,000 students across the globe achieve academic excellence through expert, human-written assessments.</p>
        <p>Our team of 1500+ PhD-qualified writers covers 120+ subjects, ensuring every student gets matched with a domain expert. We believe in transparency, quality, and delivering results that speak for themselves.</p>
        <p>We offer a unique pay-after-delivery model — you only pay once you're satisfied with the work. That's how confident we are in what we deliver.</p>
        <div class="stat-grid">
          <div class="stat-box"><div class="num"><span class="counter" data-target="180">0</span>K+</div><div class="lbl">Papers Completed</div></div>
          <div class="stat-box"><div class="num"><span class="counter" data-target="99">0</span>%</div><div class="lbl">Satisfaction Rate</div></div>
          <div class="stat-box"><div class="num"><span class="counter" data-target="1500">0</span>+</div><div class="lbl">Expert Writers</div></div>
          <div class="stat-box"><div class="num"><span class="counter" data-target="120">0</span>+</div><div class="lbl">Subjects Covered</div></div>
        </div>
      </div>
    </div>
  </div>
</section>
<section style="background:#F8FAFF">
  <div class="container">
    <div class="section-head reveal"><h2>Our Core <span>Values</span></h2><p>The principles that guide everything we do</p></div>
    <div class="values-grid reveal">
      <div class="value-card"><div class="value-icon">🎯</div><h3>Quality First</h3><p>Every piece of work goes through rigorous quality checks before delivery. We don't compromise on standards.</p></div>
      <div class="value-card"><div class="value-icon">🔒</div><h3>100% Confidential</h3><p>Your identity and personal information are completely protected. We never share client data with anyone.</p></div>
      <div class="value-card"><div class="value-icon">⚖️</div><h3>Transparency</h3><p>No hidden fees, no surprise charges. Pricing is discussed upfront and you pay only after satisfaction.</p></div>
      <div class="value-card"><div class="value-icon">🤝</div><h3>Student-First</h3><p>We understand academic pressures. Our flexible options and pay-after-delivery model are designed for you.</p></div>
      <div class="value-card"><div class="value-icon">⚡</div><h3>Always On Time</h3><p>Deadlines are sacred. We've never missed a student deadline in our 10+ years of operation.</p></div>
      <div class="value-card"><div class="value-icon">♾️</div><h3>Unlimited Revisions</h3><p>We revise until you're 100% satisfied. Your approval is the only sign-off that matters to us.</p></div>
    </div>
  </div>
</section>
<section>
  <div class="container">
    <div class="section-head reveal"><h2>Meet Our <span>Team</span></h2><p>Expert academics dedicated to your success</p></div>
    <div class="team-grid">
      <div class="team-card reveal"><div class="team-avatar">👩‍🏫</div><h3>Dr. Sarah Mitchell</h3><p>PhD, Business Management — Oxford University<br>12 years academic writing experience</p></div>
      <div class="team-card reveal" style="transition-delay:.07s"><div class="team-avatar">👨‍💻</div><h3>Prof. James Okafor</h3><p>PhD, Computer Science — Cambridge University<br>Expert in IT, AI &amp; Engineering topics</p></div>
      <div class="team-card reveal" style="transition-delay:.14s"><div class="team-avatar">👩‍⚕️</div><h3>Dr. Priya Sharma</h3><p>PhD, Nursing &amp; Healthcare — Delhi University<br>Specialist in medical &amp; nursing assignments</p></div>
      <div class="team-card reveal" style="transition-delay:.07s"><div class="team-avatar">👨‍⚖️</div><h3>Dr. Thomas Reid</h3><p>LLD, Corporate Law — Edinburgh University<br>Expert in legal research &amp; case studies</p></div>
      <div class="team-card reveal" style="transition-delay:.14s"><div class="team-avatar">👩‍💼</div><h3>Dr. Emma Chen</h3><p>PhD, Finance &amp; Economics — LSE<br>Specialist in financial modelling &amp; analysis</p></div>
      <div class="team-card reveal" style="transition-delay:.21s"><div class="team-avatar">👨‍🔬</div><h3>Dr. Ahmed Al-Farsi</h3><p>PhD, Mechanical Engineering — MIT<br>Expert in engineering design &amp; research</p></div>
    </div>
  </div>
</section>
{blue_band("Ready to Get Expert Help?", "Join 180,000+ students who have trusted us with their assessments. Get a free quote today — no obligation, instant response.", 0)}
{footer(0)}
"""
with open(f"{BASE}/about.html", "w") as f:
    f.write(page("About Us", 0, about_body))

# ── HOW IT WORKS ──────────────────────────────────────────────────────────────
how_body = f"""
<div class="page-hero">
  <h1>How It Works</h1>
  <p>A simple, transparent process designed around your needs — from first contact to final submission</p>
</div>
<section>
  <div class="container">
    <div class="section-head reveal"><h2>Our Step-by-Step <span>Process</span></h2><p>Everything you need to know about how we work</p></div>
    <div class="steps-list reveal">
      <div class="step-item">
        <div class="step-line"></div>
        <div class="step-num">1</div>
        <div class="step-content">
          <h3>Contact Us on WhatsApp</h3>
          <p>Reach out directly via WhatsApp, email, or by filling in our quote form on the website. Tell us about your assessment — subject, word count, deadline, formatting style, and any special instructions from your college.</p>
          <span class="step-tag">⚡ Instant response</span>
        </div>
      </div>
      <div class="step-item">
        <div class="step-line"></div>
        <div class="step-num">2</div>
        <div class="step-content">
          <h3>Sign Formal Agreement</h3>
          <p>Once we understand your requirements, we draw up a clear and transparent agreement covering scope, timeline, confidentiality, and revision policy. This protects both you and us from the very start.</p>
          <span class="step-tag">📄 Full protection</span>
        </div>
      </div>
      <div class="step-item">
        <div class="step-line"></div>
        <div class="step-num">3</div>
        <div class="step-content">
          <h3>Choose Your Option</h3>
          <p>You have two flexible options for how we access your materials:</p>
          <div class="options-grid" style="margin-top:16px">
            <div class="option-card">
              <div class="option-num">Option 01</div>
              <h3>You Share Materials</h3>
              <p>Upload your templates, study resources, and brief directly. You stay in control.</p>
              <ul class="option-list">
                <li>Upload templates &amp; study resources</li>
                <li>We review and begin immediately</li>
                <li>Delivered via Google Drive</li>
                <li>You submit the final work yourself</li>
              </ul>
            </div>
            <div class="option-card">
              <div class="option-num">Option 02</div>
              <h3>We Access Dashboard</h3>
              <p>Share your college login and we handle everything — downloading, completing, and even submitting.</p>
              <ul class="option-list">
                <li>Share college dashboard credentials</li>
                <li>We download all required materials</li>
                <li>We deliver via Google Drive</li>
                <li>We submit directly on your behalf</li>
              </ul>
            </div>
          </div>
          <span class="step-tag" style="margin-top:16px">🔒 Credentials handled securely</span>
        </div>
      </div>
      <div class="step-item">
        <div class="step-line"></div>
        <div class="step-num">4</div>
        <div class="step-content">
          <h3>Review Requirements &amp; Send Invoice</h3>
          <p>We thoroughly analyze your assessment brief, understand the marking criteria and learning outcomes. We then send you a transparent invoice with a clear breakdown of the cost.</p>
          <span class="step-tag">💰 No hidden charges</span>
        </div>
      </div>
      <div class="step-item">
        <div class="step-line"></div>
        <div class="step-num">5</div>
        <div class="step-content">
          <h3>We Complete Your Assessment</h3>
          <p>Our matched expert works on your assessment, ensuring it meets every requirement. Once complete, we upload it to a shared Google Drive folder and send you the link for review.</p>
          <span class="step-tag">✍️ Expert written, zero AI</span>
        </div>
      </div>
      <div class="step-item">
        <div class="step-line"></div>
        <div class="step-num">6</div>
        <div class="step-content">
          <h3>Review, Revisions &amp; Approval</h3>
          <p>You review the work and request any changes. We revise until you're fully happy. There is no limit to revision rounds — we keep going until you approve.</p>
          <span class="step-tag">♾️ Unlimited revisions</span>
        </div>
      </div>
      <div class="step-item">
        <div class="step-line"></div>
        <div class="step-num">7</div>
        <div class="step-content">
          <h3>Submission &amp; Final Payment</h3>
          <p>After final approval, we handle submission (Option 2) or share the final Drive link for you to submit (Option 1). Only after successful submission do we send the final invoice for payment.</p>
          <span class="step-tag">✅ Pay only after success</span>
        </div>
      </div>
      <div class="step-item">
        <div class="step-num">8</div>
        <div class="step-content">
          <h3>Share Your Feedback</h3>
          <p>We love hearing from happy students! Share your feedback or leave a review so we can continue improving our service and helping more students just like you.</p>
          <span class="step-tag">⭐ Leave a review</span>
        </div>
      </div>
    </div>
  </div>
</section>
{blue_band("Ready to Get Started?", "Send us a WhatsApp message and get your free quote in under 5 minutes.", 0)}
{faq_section([
  ("How quickly can you start my assessment?","We can begin within hours of receiving your requirements and agreement. For urgent orders, we prioritize immediately."),
  ("Is my login credential safe with you (Option 2)?","Absolutely. Credentials are used solely to download materials, handled by senior staff, and deleted after use. We sign a confidentiality agreement as part of our formal agreement."),
  ("What if I'm not happy with the work?","We offer unlimited free revisions. Just send your feedback and we'll rework it until you're fully satisfied. If we genuinely can't meet your requirements, we offer a full refund."),
  ("When exactly do I pay?","Payment is only requested after successful submission of the completed assessment. We work upfront — you pay after you're happy with the result."),
  ("Can I communicate with the writer?","Yes, through our team you can pass specific instructions, questions, or feedback to the expert working on your assessment at any time."),
], 0)}
{footer(0)}
"""
with open(f"{BASE}/how-it-works.html", "w") as f:
    f.write(page("How It Works", 0, how_body))

# ── CONTACT PAGE ──────────────────────────────────────────────────────────────
contact_body = f"""
<div class="page-hero">
  <h1>Contact Us</h1>
  <p>Get in touch and receive your free quote within minutes</p>
</div>
<section>
  <div class="container">
    <div class="contact-grid">
      <div class="contact-info reveal-l">
        <h2>We're Here to <span style="color:var(--blue)">Help You</span></h2>
        <p>Whether you have a question about our services, need a quick quote, or want to discuss your assessment requirements — reach out on any of the channels below. We respond within minutes.</p>
        <div class="contact-item"><div class="ci-icon">💬</div><div><div class="ci-label">WhatsApp (Fastest)</div><div class="ci-val"><a href="{WA}" target="_blank" style="color:var(--blue)">+91 98765 43210</a></div></div></div>
        <div class="contact-item"><div class="ci-icon">✉️</div><div><div class="ci-label">Email</div><div class="ci-val">help@assessmenthelp.io</div></div></div>
        <div class="contact-item"><div class="ci-icon">📞</div><div><div class="ci-label">Phone</div><div class="ci-val">+91 98765 43210 &nbsp;|&nbsp; +44 791 802 3966</div></div></div>
        <div class="contact-item"><div class="ci-icon">🕐</div><div><div class="ci-label">Availability</div><div class="ci-val">24 hours a day, 7 days a week</div></div></div>
        <a href="{WA}" target="_blank"><button class="btn-blue" style="margin-top:8px">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
          Message on WhatsApp Now
        </button></a>
      </div>
      <div class="contact-form reveal-r">
        <h3>Send Us a Message</h3>
        <form id="contactForm">
          <div class="form-group"><label>Full Name</label><input type="text" placeholder="Your full name" required></div>
          <div class="form-group"><label>Email Address</label><input type="email" placeholder="your@email.com" required></div>
          <div class="form-group"><label>Phone (WhatsApp preferred)</label>
            <div class="form-row"><select><option>IN +91</option><option>UK +44</option><option>AU +61</option><option>US +1</option></select><input type="tel" placeholder="Phone number"></div>
          </div>
          <div class="form-group"><label>Type of Service</label>
            <select><option>Assessment Help</option><option>Assignment Help</option><option>Coursework Help</option><option>Dissertation Help</option><option>Essay Writing</option><option>Other</option></select>
          </div>
          <div class="form-group"><label>Subject Area</label>
            <select><option>Management</option><option>Law</option><option>Nursing</option><option>Engineering</option><option>Accounting</option><option>IT & Computer Science</option><option>Finance & Economics</option><option>Other</option></select>
          </div>
          <div class="form-group"><label>Your Message / Requirements</label><textarea placeholder="Describe your assessment requirements, deadline, word count, etc." required></textarea></div>
          <button type="submit" class="btn-submit">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 2L11 13M22 2L15 22l-4-9-9-4 20-7z"/></svg>
            Send Message &amp; Get Free Quote
          </button>
          <div class="form-trust"><span>Free consultation</span><span>No obligation</span><span>Instant response</span></div>
        </form>
      </div>
    </div>
  </div>
</section>
{footer(0)}
"""
with open(f"{BASE}/contact.html", "w") as f:
    f.write(page("Contact Us", 0, contact_body))

# ── SERVICE PAGE GENERATOR ────────────────────────────────────────────────────
services = [
    ("assessment-help", "Assessment Help", "📝",
     "Get expert help with all types of academic assessments. Our PhD-qualified writers deliver 100% original, AI-free content tailored to your exact requirements.",
     [("✍️","Expert Writers","1500+ PhD-certified writers across all subjects and academic levels."),
      ("📄","Original Content","Every assessment written from scratch with a free plagiarism report."),
      ("⚡","Fast Turnaround","Delivery as fast as 3 hours for urgent assessment requests."),
      ("💰","Pay After Delivery","We work upfront — you only pay after you're satisfied with results.")]),
    ("assignment-help","Assignment Help","📚",
     "Struggling with assignments? Our expert writers cover every subject and deliver high-quality, well-researched content on time — every time.",
     [("🎓","PhD-Level Experts","Matched with a domain expert for your specific subject area."),
      ("⏰","On-Time Delivery","We've never missed a student deadline in 10+ years of operation."),
      ("🔄","Unlimited Revisions","Revisions until you're 100% satisfied, completely free of charge."),
      ("🔒","100% Confidential","Your details and order are fully protected and never shared.")]),
    ("coursework-help","Coursework Help","📋",
     "Get semester-long coursework support from subject experts. We handle modules, progress tracking, and every deadline along the way.",
     [("📅","Semester-Long Support","Consistent help throughout your entire coursework journey."),
      ("🧠","Module Experts","Writers who understand your specific module and requirements."),
      ("📊","Progress Tracking","Regular updates on your coursework progress and delivery timeline."),
      ("⏱️","Flexible Scheduling","Deadlines managed according to your module timeline and needs.")]),
    ("essay-writing-help","Essay Writing Help","✍️",
     "Get professionally written essays for any topic, academic level, or citation style. Human-written, well-argued, and properly referenced every time.",
     [("📖","All Citation Styles","APA, Harvard, MLA, Chicago, Vancouver — any style you need."),
      ("🔍","Deep Research","Thorough research using academic journals and credible sources."),
      ("🗣️","Original Arguments","Well-structured arguments built from scratch for your topic."),
      ("📋","Proper Structure","Introduction, body, conclusion — logically structured every time.")]),
    ("dissertation-help","Dissertation Help","🎓",
     "Expert dissertation support from topic selection through to final submission. Our PhD-level writers help you craft a dissertation that meets the highest standards.",
     [("🔬","Research Design","Help with methodology, research questions, and data collection."),
      ("📑","Chapter Writing","Individual chapter help or full dissertation writing support."),
      ("🔄","Multiple Drafts","We work through drafts with you until the final version is perfect."),
      ("📚","Literature Review","Comprehensive and critically analysed literature review writing.")]),
    ("case-study-help","Case Study Help","🔎",
     "Get expert case study analysis across business, law, nursing, and management. We break down complex cases with clear analysis and structured answers.",
     [("🏢","Business Cases","Expert analysis of real-world business scenarios and problems."),
      ("⚖️","Legal Cases","In-depth legal case analysis with correct citation and precedent."),
      ("🏥","Nursing Cases","Patient case studies written to clinical and academic standards."),
      ("📊","Data Analysis","Quantitative and qualitative data analysis for case studies.")]),
    ("online-exam-help","Online Exam Help","💻",
     "Get support with online exams, quizzes, and timed assessments. Our experts are on standby to help you perform your best under pressure.",
     [("⚡","Real-Time Help","Experts available to assist during your scheduled exam window."),
      ("🧠","Subject Specialists","Matched with experts who know your exact exam topics in depth."),
      ("🔒","100% Secure","Fully confidential service — your institution will never know."),
      ("📱","Any Platform","We work with Moodle, Canvas, Blackboard, and all other LMS platforms.")]),
]

for slug, title, icon, subtitle, ben in services:
    body = f"""
<div class="page-hero">
  <h1>{icon} {title}</h1>
  <p>{subtitle}</p>
  <div class="hero-cta">
    <button class="btn-white" onclick="location.href='../contact.html'">Get Free Quote →</button>
    <a href="{WA}" target="_blank"><button class="btn-ghost">Chat on WhatsApp</button></a>
  </div>
</div>
{ticker()}
<section>
  <div class="container">
    <div class="feature-split">
      <div class="feature-visual reveal-l">
        <div class="fv-outer"><div class="fv-inner">{icon}</div><div class="fv-badge">100% Human Written</div></div>
      </div>
      <div class="feature-text reveal-r">
        <h2>Why Choose Our <span>{title}?</span></h2>
        <p>Our team of qualified academic experts delivers tailored, original content for every order. We follow your exact instructions, meet every deadline, and revise until you're fully satisfied.</p>
        <div class="check-grid">
          <div class="check-item">PhD-qualified subject experts</div>
          <div class="check-item">100% plagiarism-free</div>
          <div class="check-item">Pay only after delivery</div>
          <div class="check-item">Unlimited free revisions</div>
          <div class="check-item">Delivered via Google Drive</div>
          <div class="check-item">24/7 WhatsApp support</div>
        </div>
        <button class="btn-blue" onclick="location.href='../contact.html'">Get My Free Quote</button>
      </div>
    </div>
  </div>
</section>
{benefits_section(ben, f'Benefits of Our {title}')}
<section style="background:#F8FAFF" id="process">
  <div class="container">
    <div class="section-head reveal"><h2>How It <span>Works</span></h2><p>Three simple steps to get started</p></div>
    <div class="process-row reveal">
      <div class="process-card"><div class="proc-icon">💬</div><h3>Contact Us</h3><p>Reach out on WhatsApp or our form with your {title.lower()} details, deadline, and requirements.</p></div>
      <div class="proc-arrow">›</div>
      <div class="process-card"><div class="proc-icon">✍️</div><h3>Expert Works on It</h3><p>We match you with a subject expert who completes your {title.lower()} to the highest standards.</p></div>
      <div class="proc-arrow">›</div>
      <div class="process-card"><div class="proc-icon">✅</div><h3>Review &amp; Submit</h3><p>Review the work, request any revisions, approve, and pay only after successful submission.</p></div>
    </div>
  </div>
</section>
{blue_band(f'Need {title}?', f'Our expert team is ready to help you achieve academic success. Get a free quote today — no obligation, instant response.', 1)}
{faq_section([
  (f"How quickly can you complete my {title.lower()}?", "Depending on length and complexity, we can deliver as fast as 3 hours for short tasks. For larger work we'll agree a realistic, reliable deadline."),
  ("Is the work 100% original?","Yes. Every piece is written from scratch by our experts. We never reuse or recycle previous work and we provide a free plagiarism report with every order."),
  ("Can I request specific changes?","Absolutely. We offer unlimited free revisions until you're completely satisfied. Just send your feedback and we'll action it immediately."),
  ("When do I pay?","We work upfront and only request payment after you've reviewed, approved, and submitted the work successfully."),
  ("How do I share my requirements?","Via WhatsApp, email, or our contact form. Share your brief, marking criteria, word count, and deadline — the more detail, the better the result."),
], 1)}
{footer(1)}
"""
    with open(f"{BASE}/services/{slug}.html", "w") as f:
        f.write(page(title, 1, body))

# ── SUBJECT PAGE GENERATOR ────────────────────────────────────────────────────
subjects = [
    ("management","Management","🏢",
     "Expert management assignment help covering HRM, strategic management, organizational behaviour, project management, and more.",
     [("🏢","Business Strategy","Strategic management, competitive analysis, and business model assignments."),
      ("👥","HRM","Human resource management, talent, and organisational behaviour topics."),
      ("📊","Project Management","PMBOK, Agile, and project planning assignment support."),
      ("🌍","International Business","Global trade, MNC strategy, and cross-cultural management help.")]),
    ("law","Law","⚖️",
     "Professional law assignment help covering corporate law, criminal law, contract law, tort, and legal case study analysis.",
     [("📜","Contract Law","Offer, acceptance, consideration — clear and well-cited contract analysis."),
      ("⚖️","Criminal Law","Criminal liability, defences, and case law analysis from experts."),
      ("🏛️","Constitutional Law","Rights, judicial review, and constitutional principles covered."),
      ("🤝","Commercial Law","Business, trade, and commercial transaction law assignments.")]),
    ("nursing","Nursing","🏥",
     "Expert nursing assignment help written to clinical and academic standards, covering patient care, pharmacology, and evidence-based practice.",
     [("💉","Clinical Nursing","Patient assessment, care plans, and clinical procedures assignments."),
      ("💊","Pharmacology","Drug interactions, dosage, and pharmacokinetics explained clearly."),
      ("📋","Evidence-Based Practice","Research-backed nursing practice analysis and critical appraisal."),
      ("🧠","Mental Health Nursing","Psychiatric nursing, mental health assessment, and intervention plans.")]),
    ("engineering","Engineering","⚙️",
     "Engineering assignment help covering mechanical, civil, electrical, and software engineering with detailed technical analysis.",
     [("⚙️","Mechanical Engineering","Thermodynamics, fluid mechanics, and mechanical design assignments."),
      ("🏗️","Civil Engineering","Structural analysis, geotechnics, and construction management help."),
      ("💡","Electrical Engineering","Circuit analysis, power systems, and electronics assignments."),
      ("💻","Software Engineering","System design, algorithms, and software architecture help.")]),
    ("accounting","Accounting","📊",
     "Expert accounting and finance assignment help covering financial statements, auditing, taxation, management accounting, and more.",
     [("📈","Financial Accounting","Balance sheets, income statements, and IFRS/GAAP compliance help."),
      ("📉","Management Accounting","Budgeting, variance analysis, and cost accounting assignments."),
      ("🔍","Auditing","Audit procedures, risk assessment, and internal controls analysis."),
      ("💰","Taxation","Corporate and individual tax computation and planning assignments.")]),
    ("it-computer-science","IT & Computer Science","💻",
     "Expert IT and computer science assignment help covering programming, databases, networking, cybersecurity, AI, and software development.",
     [("🐍","Programming","Python, Java, C++, JavaScript — code written and explained clearly."),
      ("🗄️","Databases","SQL, NoSQL, database design, and data modelling assignments."),
      ("🔐","Cybersecurity","Network security, ethical hacking concepts, and cryptography help."),
      ("🤖","AI & Machine Learning","ML algorithms, neural networks, and AI project assignments.")]),
    ("finance-economics","Finance & Economics","💹",
     "Expert finance and economics assignment help covering macroeconomics, financial modelling, investment analysis, and econometrics.",
     [("📊","Financial Modelling","DCF, valuation models, and financial projections for assignments."),
      ("🌍","Macroeconomics","GDP, inflation, monetary policy, and fiscal policy analysis."),
      ("📈","Investment Analysis","Portfolio theory, risk management, and asset valuation help."),
      ("📉","Econometrics","Regression analysis, statistical modelling, and data interpretation.")]),
]

for slug, title, icon, subtitle, ben in subjects:
    body = f"""
<div class="page-hero">
  <h1>{icon} {title} Assignment Help</h1>
  <p>{subtitle}</p>
  <div class="hero-cta">
    <button class="btn-white" onclick="location.href='../contact.html'">Get Free Quote →</button>
    <a href="{WA}" target="_blank"><button class="btn-ghost">Chat on WhatsApp</button></a>
  </div>
</div>
{ticker()}
<section>
  <div class="container">
    <div class="feature-split">
      <div class="feature-visual reveal-l">
        <div class="fv-outer"><div class="fv-inner">{icon}</div><div class="fv-badge">100% Human Written</div></div>
      </div>
      <div class="feature-text reveal-r">
        <h2>Expert <span>{title} Help</span></h2>
        <p>Our {title.lower()} specialists are PhD-qualified academics with years of real-world and academic experience. They deliver original, well-researched assignments tailored to your exact module requirements.</p>
        <div class="check-grid">
          <div class="check-item">PhD {title} specialists</div>
          <div class="check-item">100% plagiarism-free</div>
          <div class="check-item">Correct referencing</div>
          <div class="check-item">Unlimited free revisions</div>
          <div class="check-item">Pay after delivery only</div>
          <div class="check-item">24/7 WhatsApp support</div>
        </div>
        <button class="btn-blue" onclick="location.href='../contact.html'">Get My Free Quote</button>
      </div>
    </div>
  </div>
</section>
{benefits_section(ben, f'Why Students Choose Our {title} Help')}
{blue_band(f'Need {title} Assignment Help?', f'Our {title.lower()} experts are ready to help you achieve academic success. Free quote in minutes — pay only after you are satisfied.', 1)}
{faq_section([
  (f"Do you have real {title} experts?",f"Yes. Every {title.lower()} assignment is handled by a PhD-qualified specialist who has studied and worked in the field. We never assign work to generalists."),
  ("How do I share my assignment details?","Simply WhatsApp us or fill in our contact form. Share the brief, marking rubric, word count, deadline, and any module-specific guidelines."),
  ("What citation styles do you use?","We work with any citation style — APA, Harvard, MLA, OSCOLA (for Law), Vancouver (for Nursing), IEEE (for Engineering) — just let us know."),
  ("Can I get help with just one section?","Yes! You can request help with a specific chapter, section, or question. We're flexible and work to your exact needs."),
  ("When do I pay?","Only after you've reviewed, approved the work, and it's been successfully submitted. We work upfront — you pay after satisfaction."),
], 1)}
{footer(1)}
"""
    with open(f"{BASE}/subjects/{slug}.html", "w") as f:
        f.write(page(f"{title} Assignment Help", 1, body))

print("✅ All pages generated successfully!")
files = []
for root, dirs, filenames in os.walk(BASE):
    for fn in filenames:
        if fn.endswith('.html'):
            files.append(os.path.join(root,fn).replace(BASE+'/',''))
print(f"Total HTML pages: {len(files)}")
for f in sorted(files):
    print(f" • {f}")

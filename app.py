from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Karan | Itachii-Dev</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#0a0a0a;color:#fff;font-family:'Segoe UI',sans-serif;overflow-x:hidden;}
nav{position:fixed;top:0;width:100%;background:rgba(10,10,10,0.9);backdrop-filter:blur(10px);padding:15px 30px;display:flex;justify-content:space-between;align-items:center;z-index:100;border-bottom:1px solid #1a1a1a;}
.logo{color:#00d4ff;font-weight:bold;font-size:1.2em;}
.nav-links a{color:#ccc;text-decoration:none;margin-left:20px;font-size:.9em;transition:.3s;}
.nav-links a:hover{color:#00d4ff;}
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:80px 20px 40px;background:radial-gradient(ellipse at center,#0d1b2a 0%,#0a0a0a 70%);}
.hero-content h1{font-size:2.5em;margin-bottom:10px;}
.hero-content h1 span{color:#00d4ff;}
.typing{font-size:1.2em;color:#00d4ff;margin:10px 0;}
.hero-content p{color:#aaa;margin:15px 0;max-width:500px;}
.btn{display:inline-block;background:linear-gradient(135deg,#00d4ff,#0099cc);color:#000;padding:12px 30px;border-radius:25px;text-decoration:none;font-weight:bold;margin:10px;transition:.3s;}
.btn:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(0,212,255,0.3);}
.btn-outline{background:transparent;color:#00d4ff;border:2px solid #00d4ff;}
.btn-outline:hover{background:#00d4ff;color:#000;}
section{padding:80px 20px;}
.section-title{text-align:center;font-size:2em;margin-bottom:50px;}
.section-title span{color:#00d4ff;}
.skills-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:20px;max-width:700px;margin:auto;}
.skill-card{background:#111;border:1px solid #1a1a1a;border-radius:15px;padding:25px 15px;text-align:center;transition:.3s;}
.skill-card:hover{border-color:#00d4ff;transform:translateY(-5px);}
.skill-icon{font-size:2em;margin-bottom:10px;}
.skill-card p{color:#aaa;font-size:.85em;}
.projects-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:25px;max-width:900px;margin:auto;}
.project-card{background:#111;border:1px solid #1a1a1a;border-radius:15px;padding:25px;transition:.3s;}
.project-card:hover{border-color:#00d4ff;transform:translateY(-5px);}
.project-tag{background:rgba(0,212,255,0.1);color:#00d4ff;padding:4px 12px;border-radius:20px;font-size:.8em;margin-right:5px;}
.project-card h3{margin:15px 0 10px;}
.project-card p{color:#aaa;font-size:.9em;line-height:1.6;}
.project-links{margin-top:15px;}
.project-links a{color:#00d4ff;text-decoration:none;margin-right:15px;font-size:.9em;}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:600px;margin:0 auto 60px;}
.stat{text-align:center;background:#111;padding:25px;border-radius:15px;border:1px solid #1a1a1a;}
.stat h3{font-size:2em;color:#00d4ff;}
.stat p{color:#aaa;font-size:.85em;}
.contact-section{background:#0d0d0d;text-align:center;}
.contact-btn{display:inline-block;background:#25D366;color:#fff;padding:15px 40px;border-radius:25px;text-decoration:none;font-size:1.1em;margin:10px;transition:.3s;}
.contact-btn:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(37,211,102,0.3);}
.github-btn{background:#333;}
.github-btn:hover{box-shadow:0 10px 30px rgba(255,255,255,0.1);}
footer{text-align:center;padding:30px;color:#555;border-top:1px solid #1a1a1a;}
</style>
</head>
<body>
<nav>
  <div class="logo">&lt;ITACHII-DEV/&gt;</div>
  <div class="nav-links">
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
  </div>
</nav>
<section class="hero">
  <div class="hero-content">
    <h1>Hey, I'm <span>Karan</span> 👋</h1>
    <div class="typing">Python Developer & Bot Maker 🔥</div>
    <p>Main phone se bots aur websites banata hoon jo real kaam karte hain. Termux se lekar Render tak!</p>
    <a href="#projects" class="btn">My Projects</a>
    <a href="#contact" class="btn btn-outline">Hire Me</a>
  </div>
</section>
<section id="skills">
  <h2 class="section-title">My <span>Skills</span></h2>
  <div class="skills-grid">
    <div class="skill-card"><div class="skill-icon">🐍</div><b>Python</b><p>Core language</p></div>
    <div class="skill-card"><div class="skill-icon">🌐</div><b>Flask</b><p>Web framework</p></div>
    <div class="skill-card"><div class="skill-icon">🤖</div><b>Telegram Bot</b><p>Automation</p></div>
    <div class="skill-card"><div class="skill-icon">📱</div><b>Termux</b><p>Mobile dev</p></div>
    <div class="skill-card"><div class="skill-icon">🐙</div><b>GitHub</b><p>Version control</p></div>
    <div class="skill-card"><div class="skill-icon">☁️</div><b>Render</b><p>Deployment</p></div>
  </div>
</section>
<section id="projects">
  <h2 class="section-title">My <span>Projects</span></h2>
  <div class="projects-grid">
    <div class="project-card">
      <span class="project-tag">Python</span><span class="project-tag">Flask</span>
      <h3>🌐 Portfolio Website</h3>
      <p>Personal portfolio website built with Flask, deployed on Render. Phone se banaya aur host kiya!</p>
      <div class="project-links">
        <a href="https://myportfolio-52m4.onrender.com">🔗 Live Demo</a>
        <a href="https://github.com/ITACHII-DEV/myportfolio">📁 GitHub</a>
      </div>
    </div>
    <div class="project-card">
      <span class="project-tag">Python</span><span class="project-tag">Telegram</span>
      <h3>🤖 Telegram Bot</h3>
      <p>Auto-reply aur automation bot. Smart responses aur custom commands ke saath!</p>
      <div class="project-links">
        <a href="https://github.com/ITACHII-DEV">📁 GitHub</a>
      </div>
    </div>
  </div>
</section>
<section id="contact" class="contact-section">
  <h2 class="section-title">Get In <span>Touch</span></h2>
  <p style="color:#aaa;margin-bottom:30px;">Bot banana hai? Website chahiye? Contact karo!</p>
  <a href="https://wa.me/917643959056" class="contact-btn">💬 WhatsApp</a>
  <a href="https://github.com/ITACHII-DEV" class="contact-btn github-btn">🐙 GitHub</a>
</section>
<footer>
  <p>Built with ❤️ by Karan aka ITACHII-DEV | Phone se banaya 📱</p>
</footer>
</body>
</html>"""

app.run(host="0.0.0.0", port=5000)

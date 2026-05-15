from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Karan | Itachii-Dev</title>
<style>
  body{margin:0;background:#0d0d0d;color:#fff;font-family:Arial;}
  .hero{text-align:center;padding:60px 20px;background:linear-gradient(135deg,#1a1a2e,#16213e);}
  h1{font-size:2em;color:#00d4ff;}
  .badge{background:#00d4ff;color:#000;padding:5px 15px;border-radius:20px;font-size:.9em;}
  .section{padding:30px 20px;max-width:600px;margin:auto;}
  .skill-box{display:inline-block;background:#1e1e2e;border:1px solid #00d4ff;padding:8px 16px;margin:5px;border-radius:8px;}
  .project{background:#1e1e2e;padding:15px;margin:10px 0;border-radius:10px;border-left:3px solid #00d4ff;}
  .contact-btn{display:block;background:#25D366;color:#fff;text-align:center;padding:15px;border-radius:10px;text-decoration:none;font-size:1.1em;margin:10px 0;}
</style>
</head>
<body>

<div class="hero">
  <h1>🔥 KARAN AKA ITACHII-DEV</h1>
  <span class="badge">Python Developer</span>&nbsp;
  <span class="badge">Bot Maker</span>
  <p>Main bots banata hoon jo kaam karte hain 💪</p>
</div>

<div class="section">
  <h2>⚡ Skills</h2>
  <div class="skill-box">Python</div>
  <div class="skill-box">Flask</div>
  <div class="skill-box">Telegram Bot</div>
  <div class="skill-box">GitHub</div>
  <div class="skill-box">Termux</div>

  <h2>🚀 Projects</h2>
  <div class="project">
    <b>Portfolio Website</b><br>
    <small>Phone se serve hone wali Flask website</small>
  </div>
  <div class="project">
    <b>Telegram Bot</b><br>
    <small>Auto-reply aur automation bot</small>
  </div>

  <h2>📞 Contact</h2>
  <a class="contact-btn" href="https://wa.me/917643959056">💬 WhatsApp Pe Message Karo</a>
</div>

</body>
</html>
"""

app.run(host="0.0.0.0", port=5000)

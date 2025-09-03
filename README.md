<h1>FlyFF Automation Bot</h1>

<img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python">

<h2>Description</h2>
<p>
Tool designed to automate repetitive tasks in the MMORPG <strong>FlyFF</strong>. 
It uses <strong>PyAutoGUI</strong> to recognize in-game elements and simulate player actions, helping with pet feeding, healing, and buff management. 
Ideal for learning automation with Python and experimenting with game bots in a safe, educational environment.
</p>

<h2>Features</h2>
<ul>
 <li>
<strong>Auto Pet Feed:</strong> Automatically detects when your pet needs feeding and performs the action. It includes the following precautions:
  <ol>
    <li>Prevents your pet from starving if the pet feed runs out.</li>
    <li>Avoids wasting pet feed when the pet reaches 99.99% XP.</li>
    <li>Handles cases where the pet is unequipped by mistake.</li>
  </ol>
</li>
  <li><strong>Auto Heal:</strong> Monitors character HP and triggers healing as needed.</li>
  <li><strong>Auto Buff:</strong> Applies buffs in a configurable sequence via a global hotkey.</li>
  <li><strong>Active Window Selection:</strong> Allows sending commands to a specific game window, even with multiple windows open.</li>
</ul>

<h2>Technologies</h2>
<ul>
  <li>Python</li>
  <li>PyAutoGUI</li>
  <li>PyWin32 (for Windows interactions)</li>
</ul>

<h2>Setup</h2>
<ol>
  <li>
    <strong>Clone the repository:</strong>
    <pre><code>git clone</code></pre>
  </li>
  <li>
    <strong>Install dependencies:</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ol>

<h2>Configuration</h2>
<p>
All input settings for the bot's functions (hotkeys, sequences, etc.) are stored in JSON files. 
You can customize these settings by editing the JSON files directly to suit your preferences.
</p>
<h2>Usage</h2>
<ol>
  <li>
    Run the main script:
    <pre><code>python bot.py</code></pre>
  </li>
  <li>Follow on-screen instructions to select the FlyFF game window.</li>
  <li>Use configured hotkeys to activate specific features (e.g., auto buffs).</li>
  <li>
    
<strong>Important:</strong> The script must be run as Administrator, or the OS may block simulated inputs. 
<br>If you have difficulty running it normally as Administrator, you can also run it from VSCode, 
but in this case VSCode itself must be running as Administrator. (This was the easiest method in our testing.)
</li>
</ol>

<h2>Notes</h2>
<ul>
  <li>This bot is intended <strong>for educational and experimental purposes only</strong>.</li>
  <li>Some FlyFF servers may not allow the use of bots or automation tools. 
<br>(Users should check the rules of the specific server they are playing on before using this bot to ensure it is permitted.)</li>
</ul>

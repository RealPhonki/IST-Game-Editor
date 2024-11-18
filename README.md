<div align="center">
<pre>
██╗███████╗████████╗     ██████╗  █████╗ ███╗   ███╗███████╗    ███████╗██████╗ ██╗████████╗ ██████╗ ██████╗ 
██║██╔════╝╚══██╔══╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔════╝██╔══██╗██║╚══██╔══╝██╔═══██╗██╔══██╗
██║███████╗   ██║       ██║  ███╗███████║██╔████╔██║█████╗      █████╗  ██║  ██║██║   ██║   ██║   ██║██████╔╝
██║╚════██║   ██║       ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██╔══╝  ██║  ██║██║   ██║   ██║   ██║██╔══██╗
██║███████║   ██║       ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████╗██████╔╝██║   ██║   ╚██████╔╝██║  ██║
╚═╝╚══════╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
</pre>
</div>

## About
This is a map editor specifically made for a <a href="https://scratch.mit.edu/projects/1008872842/">game made in scratch<a>, feel free to check it out.
(Since the project is of a small scale and so specific, I didn't bother making the code reuseable or readable)

## Setup
1. Make sure you have python installed, you can check with these shell commands:
```sh
python --version
pip --version
```
2. Copy the zip file and extract it, or clone the repository with this shell command:
```sh
git clone https://github.com/RealPhonki/IST-Game-Editor.git
```
3. (optional) Create a virtual environment and activate it with these shell commands:
```sh
python3 -m venv .venv
source .venv/bin/activate
```
4. Install dependencies with this shell command (you will need to have an internet connection):
```sh
pip3 install -r requirements.txt
```
5. Run the code with this command, (you will need to be in the same directory as the main.py file) or click `Run` in the code editor of your choice:
```sh
python3 main.py
```

## Usage
### Tile Keybinds:
- `1`: Delete tiles
- `2`: Place tiles
- `3`: Place obstacles (blue blocks)
- `4`: Place player spawn (2 maximum)
- `5`: Place goal (1 maximum)

- `Middle click`: Move the camera
- `Left click` Place object
- `Z`: Remove row (from bottom)
- `C`: Add row (from bottom)
- `Q`: Remove column (from right)
- `E`: add column (from right)
- `Enter/Return`: Export the map to txt files located in the `out` directory

### Export
Once the map is exported do the following the play your level:
1. Open up the scratch project
2. Paste the contents of `out/map.txt` into any slot in `Map List` in the scratch project (the other slots need to the same)
3. Paste the contents of `out/obstacles.txt` into the same slot as in step 1 in `Obstacle List` in the scratch project
4. Paste the contents of `out/goal-list.txt` into the same slot as in step 1 in `Goal List` in the scratch project
5. Play the game to reach the level you overrode/added

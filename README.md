# Topic Detection on Steam Video Games using Latent Dirichlet Allocation
### Akshay Srivatsan - asrivat1@jhu.edu

## Overview:

The goal of this project was to use the Latent Dirichlet Allocation model to perform topic detection on video games in the Steam library.

![Image of Steam](http://img2.wikia.nocookie.net/__cb20110823175948/logopedia/images/a/ae/Steam_logo.svg)

Steam is a video game marketplace with 125 million active users that hosts thousands of popular games for PC. Each game on Steam has a corresponding web page that contains a brief description of the title, some keywords, some technical specifications, and finally several user written reviews. Each page also provides a link to twelve games deemed similar by Steam's own recommendation system. This inherent connectedness can be interpreted as a graph with games as nodes and links as edges. We can then scrape this graph using a breadth first search.

![Image of LDA](http://upload.wikimedia.org/wikipedia/commons/d/d3/Latent_Dirichlet_allocation.svg)

Once we have the text from the html of the pages, we can do topic detection using the LDA model. In the LDA model, we take the approach that each word in each document is related to one of K different topics.

## Results:

I obtained the following results on a dataset of 1247 titles, using 25 topics, parameters 0.1 and 0.01 for alpha and beta respectively, and 1100 iterations of which 1000 were spent burning in the sampling chain to a stable state.

### Common Words in Topics

**Topic 0:**
rpg  
combat
character
world
quests
system
skills
quest
level
characters
magic
items
heroes
skill
party

**Topic 1:**  
weapons
zombies
dead
guns
zombie
enemies
fps
survival
gun
weapon
shooter
kill
ammo
combat
map

**Topic 2:**  
life
half
needed
wood
coo
counter
strike
source
need
valve
episode
radio
fire
backup
portal

**Topic 3:**  
gb
hd
nvidia
dlc
intel
pack
geforce
radeon
core
amd
edition
ati
windows
series
ghz

**Topic 4:**  
turn
based
strategy
tactical
combat
enemy
units
tactics
missions
campaign
space
games
battle
mission
board

**Topic 5:**  
game
fixed
added
steam
update
release
issues
version
support
bugs
updates
games
fix
mode
comments

**Topic 6:**  
review
helpful
funny
found
reviews
game
people
read
recommended
account
yes
record
products
posted
hrs

**Topic 7:**  
game
time
don
make
ve
re
play
want
need
back
bad
start
ll
things
review

**Topic 8:**  
war
units
strategy
total
battle
campaign
ai
ii
unit
battles
pack
empire
multiplayer
army
men

**Topic 9:**  
levels
level
music
platformer
puzzle
soundtrack
platforming
jump
controls
world
hard
simple
challenging
indie
controller

**Topic 10:**  
enemies
mode
game
action
fun
boss
characters
controller
fighting
attack
combat
character
arcade
enemy
level

**Topic 11:**  
story
characters
adventure
point
character
games
click
voice
series
acting
art
dialogue
plot
game
original

**Topic 12:**  
stealth
metro
funny
prison
shadow
cell
starve
clean
night
la
day
november
people
guards
blood

**Topic 13:**  
sonic
tower
defense
civilization
strategy
games
civ
game
defenders
map
endless
towers
units
research
ai

**Topic 14:**  
space
ship
ships
planet
add
combat
star
galaxy
planets
simulator
train
universe
system
build
fleet

**Topic 15:**  
early
access
review
game
build
april
development
building
world
crafting
community
features
alpha
feedback
version

**Topic 16:**  
hat
cards
card
play
deck
magic
free
pay
pvp
mmo
money
players
online
player
win

**Topic 17:**  
enemy
spotted
city
cities
people
building
simulator
build
simulation
world
tropico
bridge
money
buildings
motion

**Topic 18:**  
game
games
gameplay
good
great
pretty
graphics
feel
experience
find
nice
bit
interesting
player
reviews

**Topic 19:**  
game
players
play
team
player
review
free
friends
multiplayer
people
fun
online
community
match
maps

**Topic 20:**  
racing
cars
lego
car
batman
race
physics
driving
tracks
simulator
track
series
truck
drive
city

**Topic 21:**  
dungeon
items
rogue
enemies
die
roguelike
fun
monsters
generated
run
loot
randomly
random
isaac
dungeons

**Topic 22:**  
nope
horror
atmosphere
story
myst
experience
puzzles
dark
world
arcade
exploration
played
scary
explore
anarchy

**Topic 23:**  
puzzles
puzzle
hidden
object
ve
games
story
solve
adventure
click
objects
post
gb
point
command

**Topic 24:**  
original
wars
star
classic
doom
ii
jedi
ys
knight
force
years
great
played
edition
version

### Documents with High Proportion of Topics

**Topic 0:**  
Breath of Death VII  
The Book of Legends  
Cthulhu Saves the World  
Divine Divinity  
Sacred 2 Gold  
The Incredible Adventures of Van Helsing  
Sacred Gold  
Divinity II: Developer's Cut  
Asguaard  
Titan Quest - Immortal Throne  
Gothic II: Gold Edition  
Knights of Pen and Paper +1 Edition  
WAKFU  
Torchlight II  
The Incredible Adventures of Van Helsing II  

**Topic 1:**  
Rising Storm Game of the Year Edition  
S.T.A.L.K.E.R.: Call of Pripyat  
Dying Light  
theHunter: Primal  
Red Orchestra: Ostfront 41-45  
Serious Sam 3: BFE  
No More Room in Hell  
National Zombie Park  
This War of Mine  
Enemy Front  
Serious Sam Classic: The First Encounter  
Contagion  
Dead Pixels  
Serious Sam Classic: The Second Encounter  
Receiver  

**Topic 2:**  
Stronghold Crusader HD  
Counter-Strike: Source  
Half-Life: Blue Shift  
Hatoful Boyfriend  
Half-Life 2: Episode Two  
Half-Life 2  
Half-Life 2: Lost Coast  
Half-Life 2: Episode One  
Half-Life: Source  
Half-Life  
Half-Life: Opposing Force  
Counter-Strike: Condition Zero  
Counter-Strike: Global Offensive  
Counter-Strike  
Team Fortress Classic  

**Topic 3:**  
Street Fighter X Tekken  
Call of Duty: Black Ops III  
Toren  
Ultra Street Fighter IV  
Worms Revolution  
Worms Reloaded  
Legend of Kay Anniversary  
The Witcher 3: Wild Hunt  
F1 2013  
Painkiller Hell & Damnation  
Call of Duty: Modern Warfare 2  
Worms Ultimate Mayhem  
Might & Magic: Heroes VI  
Transformers: Fall of Cybertron  
Worms Clan Wars  

**Topic 4:**  
Mordheim: City of the Damned  
Space Hulk  
Space Hulk Ascension  
WARMACHINE: Tactics  
Warhammer 40,000: Regicide  
Warhammer 40,000: Armageddon  
Talisman: Prologue  
Warhammer 40,000: Dawn Of War  Winter Assault  
Blood Bowl Legendary Edition  
Frozen Synapse  
Shadowrun: Dragonfall - Director's Cut  
Bionic Dues  
Chainsaw Warrior  
Jagged Alliance 2 Gold  
Hell  

**Topic 5:**  
Gang Beasts  
GameGuru  
Pool Nation  
Castle Story  
BeamNG.drive  
Cities XXL  
Tabletop Simulator  
Universe Sandbox  
CDF Ghostship  
Planetary Annihilation  
Audiosurf 2  
Cities: Skylines  
Just Cause 3  
Spacebase DF-9  
Trine 3: The Artifacts of Power  

**Topic 6:**  
Plug & Play  
Floating Point  
The Basement Collection  
Super Crate Box  
The Impossible Game  
Jagged Alliance 2 Gold  
Toki Tori  
Faerie Solitaire  
AudioSurf  
Counter-Strike  
LEGO Star Wars - The Complete Saga  
Half-Life 2: Lost Coast  
Universe Sandbox  
Sonic the Hedgehog  
AdVenture Capitalist  

**Topic 7:**  
Vindictus  
Streets of Chaos  
Always Sometimes Monsters  
This War of Mine  
Football Manager 2015  
Zafehouse: Diaries  
Windforge  
SUNLESS SEA  
The Age of Decadence  
Fiesta Online NA  
Wasteland 1 - The Original Classic  
Broken Age  
Elite: Dangerous  
Firefall  
MapleStory  

**Topic 8:**  
Empire: Total War  
Crusader Kings II  
Men of War: Assault Squad  
Hearts of Iron III  
Medieval II: Total War  
Total War: Shogun 2 - Fall of the Samurai  
Napoleon: Total War  
Rome: Total War  
Panzer Corps  
Men of War  
Europa Universalis III Complete  
To End All Wars  
Total War: ROME II - Emperor Edition  
Commander: The Great War  
Europa Universalis IV  

**Topic 9:**  
Giana Sisters: Twisted Dreams  
BIT.TRIP Presents... Runner2: Future Legend of Rhythm Alien  
Giana Sisters: Twisted Dreams - Rise of the Owlverlord  
BIT.TRIP RUNNER  
Fly'N  
Electronic Super Joy  
Fermi's Path  
Super Puzzle Platformer Deluxe  
Offspring Fling!  
Soundodger+  
BIT.TRIP BEAT  
1001 Spikes  
Dustforce DX  
Beatbuddy: Tale of the Guardians  
JumpJet Rex  

**Topic 10:**  
Divekick  
Mitsurugi Kamui Hikae  
Devil May Cry 3 Special Edition  
Kung Fu Strike - The Warrior's Rise  
GundeadliGne  
Aqua Kitty - Milk Mine Defender  
GIGANTIC ARMY  
Megabyte Punch  
Waves  
One Finger Death Punch  
Vanguard Princess  
Devil May Cry 4  
Phantom Breaker: Battle Grounds  
Super Galaxy Squadron  
Ultratron  

**Topic 11:**  
Blackwell Unbound  
Blackwell Convergence  
The Blackwell Legacy  
Edna & Harvey: Harvey's New Eyes  
Goodbye Deponia  
Blackwell Deception  
Dreamfall Chapters  
Randal's Monday  
Broken Sword 5 - the Serpent's Curse  
Broken Sword: Director's Cut  
Chaos on Deponia  
The Next BIG Thing  
Deponia  
Monkey Island 2 Special Edition: LeChucks Revenge  
The Cat Lady  

**Topic 12:**  
Viscera Cleanup Detail: Santa's Rampage  
Surgeon Simulator 2013  
Prison Architect  
Viscera Cleanup Detail: Shadow Warrior  
Five Nights at Freddy's 2  
Viscera Cleanup Detail  
Five Nights at Freddy's  
TrackMania Nations Forever  
Cook, Serve, Delicious!  
100% Orange Juice  
The Escapists  
I am Bread  
Tom Clancys Splinter Cell Blacklist  
Octodad: Dadliest Catch  
Little Inferno  

**Topic 13:**  
Sonic the Hedgehog 2  
Sonic 3 and Knuckles  
Sonic the Hedgehog  
Sid Meier's Civilization: Beyond Earth  
Civilization IV: Beyond the Sword  
DG2: Defense Grid 2  
Sid Meier's Civilization IV: Colonization  
Dungeon Defenders  
Endless Legend  
Revenge of the Titans  
Sonic CD  
Sonic Generations  
Sonic the Hedgehog 4 - Episode II  
Sid Meier's Civilization V  
Galactic Civilizations II: Ultimate Edition  

**Topic 14:**  
Train Simulator 2015  
X2: The Threat  
X Rebirth  
Evochron Mercenary  
Distant Worlds: Universe  
X3: Reunion  
Elite: Dangerous  
Space Pirates and Zombies 2  
X3: Terran Conflict  
Galaxy on Fire 2 Full HD  
Out There:  Edition  
X: Beyond the Frontier  
Strike Suit Zero  
Horizon  
Kerbal Space Program  

**Topic 15:**  
Medieval Engineers  
Rising World  
Oort Online  
Stranded Deep  
Subnautica  
FortressCraft Evolved!  
Eden Star :: Destroy - Build - Protect  
Savage Lands  
GRAV  
Predestination  
Salt  
Landmark  
Blockscape  
Xsyon - Prelude  
Beasts of Prey  

**Topic 16:**  
Team Fortress 2  
Magic: The Gathering - Duels of the Planeswalkers 2013  
Magic 2014  Duels of the Planeswalkers  
Kingdoms CCG  
Nightbanes  
Magic: The Gathering - Duels of the Planeswalkers 2012  
SolForge  
Magic 2015 - Duels of the Planeswalkers  
Might & Magic: Duel of Champions  
Pox Nora  
Infinity Wars 2014: Animated Trading Card Game  
Ragnarok Online 2  
BloodRealm: Battlegrounds  
Royal Quest  
Battlegrounds of Eldhelm  

**Topic 17:**  
Battlefield 2: Complete Collection  
Moonbase Alpha  
Cities in Motion  
Train Simulator: South London Network Route Add-On  
Tropico 4: Steam Special Edition  
The Race for the White House  
Train Fever  
Cities in Motion 2  
Riding Star  
Tropico 3 - Steam Special Edition  
Masters of the World - Geopolitical Simulator 3  
Democracy 3  
Banished  
SimCity 4 Deluxe Edition  
Tropico 5  

**Topic 18:**  
Aquaria  
Claire  
Full Bore  
Forward to the Sky  
The Old City: Leviathan  
The Swapper  
NightSky  
Brothers - A Tale of Two Sons  
A Story About My Uncle  
Mind: Path to Thalamus  
FRACT OSC  
Styx: Master of Shadows  
Closure  
Skyborn  
NaissanceE  

**Topic 19:**  
Awesomenauts  
Strife  
Solstice Arena  
HAWKEN  
AirMech  
Quake Live  
Super MNC  
Warface  
Freestyle2: Street Basketball  
AERENA - Masters Edition  
Infinite Crisis  
GunZ 2: The Second Duel  
Blacklight: Retribution  
Block N Load  
Sins of a Dark Age  

**Topic 20:**  
Assetto Corsa  
GRID Autosport  
RaceRoom Racing Experience  
Need For Speed: Hot Pursuit  
Euro Truck Simulator 2  
GRID 2  
Euro Truck Simulator  
DiRT Showdown  
The Crew  
Project CARS  
LEGO Batman3: Beyond Gotham  
Driver San Francisco  
Copa Petrobras de Marcas  
LEGO Batman 2 DC Super Heroes  
Gotham City Impostors Free to Play  

**Topic 21:**  
Ziggurat  
Rogue Legacy  
Diehard Dungeon  
The Binding of Isaac: Rebirth  
Our Darker Purpose  
Sword of the Stars: The Pit  
Full Mojo Rampage  
Legend of Dungeon  
Dungeons of Dredmor  
Enter the Gungeon  
Hack, Slash, Loot  
Saints Row: Gat out of Hell  
A Wizard's Lizard  
Dungeonmans  
Overture  

**Topic 22:**  
Cry of Fear  
Anarchy Arcade  
Outlast  
The Fall  
Risk of Rain  
Cylne  
Among the Sleep  
Slender: The Arrival  
Amnesia: A Machine for Pigs  
Neverending Nightmares  
Claire  
Botanicula  
NaissanceE  
Amnesia: The Dark Descent  
Passing Pineview Forest  

**Topic 23:**  
STAR WARS Battlefront II  
Enigmatis: The Ghosts of Maple Creek  
Grim Legends: The Forsaken Bride  
Time Mysteries 2: The Ancient Spectres  
Nightmares from the Deep 2: The Siren`s Call  
Nightmares from the Deep: The Cursed Heart  
Time Mysteries: Inheritance - Remastered  
9 Clues: The Secret of Serpent Creek  
Nightmares from the Deep 3: Davy Jones  
Demon Hunter: Chronicles from Beyond  
Left in the Dark: No One on Board  
Clockwork Tales: Of Glass and Ink  
Grim Legends 2: Song of the Dark Swan  
Enigmatis 2: The Mists of Ravenwood  
Abyss: The Wraiths of Eden  

**Topic 24:**  
STAR WARS Jedi Knight - Mysteries of the Sith  
STAR WARS Jedi Knight - Dark Forces II  
STAR WARS Jedi Knight II - Jedi Outcast  
STAR WARS Jedi Knight - Jedi Academy  
STAR WARS - Dark Forces  
STAR WARS - The Force Unleashed II  
STAR WARS - The Force Unleashed Ultimate Sith Edition  
STAR WARS Knights of the Old Republic II - The Sith Lords  
Wolfenstein 3D  
Deus Ex: Mankind Divided  
Tomb Raider: Anniversary  
Oddworld: Abe's Exoddus  
STAR WARS Empire at War - Gold Pack  
Baldur's Gate II: Enhanced Edition  
Final DOOM  

## Discussion:

## Usage:

First run grab_info_steam.py to scrape the Steam library for data. You can terminate that process whenever you like, but I found that good results were obtained after scraping ~1200 titles, which may take close to half an hour depending on connectivity.

Then run run-LDA.sh to do inference on the LDA model using the collected data. In the results I have included, I ran it using K=25, alpha=0.1, beta=0.01, T=1100, and burnin=1000. The names of the input and output files are games and steam respectively.

You can then rune analyze.py to print out a brief summary of the parameters that the model has learned. It takes as arguments the name file and output file which are called games-names and steam respectively by default.

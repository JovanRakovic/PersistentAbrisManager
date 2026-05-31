<h1>Description</h1>
PersistentAbris is a solution to the problem of losing all your routes, additional info and nav data in the Ka-50 when leaving a mission or server.

The solution to making all the routes and map info persistent accross missions is to modify the ABRIS.lua file, which is responsible for saving and loading said data, so that is saves all the data to a set of files in a location in the SavedGames DCS directory, where it will also read them from. From testing, this does not appear to break the integrity check, so you should be able to fly on any server.

<b>Note: Currently, if a mission has baked in abris data, your persistent files will not be loaded for that mission. I have tried a couple of ways of getting around this issue, but have yet to find a solution</b>

With just the steps described above, you would have a single set of files containing all your routes, additional info and nav data, which would accumulate quite a collection given enough time. Given that you would probably want to avoid having a massive amount of routes and possibly conflicting or inaccurate map elements, I have developed a manager app to work alongside the modified ABRIS.lua file. Keep in mind that you do not need the manager app for the persistent data to work, only to manage what you load and save in an easier fassion.

<h1>Installation</h1>
As said before, you will need to do two things to make PersistentAbris work: overwrite the ABRIS.lua file with the modified version and make a certain folder structure inside the SavedGames DCS directory.

There are two ways of doing this:
<ol>
  <li>Manualy</li>
  <li>Via the manager app (Recommended)</li>
</ol>

<h3>Manual method</h3>
<ol>
  <li>Download the modified ABRIS.lua file from the repository above</li>
  <li>Repalce the original ABRIS.lua file in "[your dcs root directory]/Mods/aircraft/Ka-50_3/Cockpit/Scripts/Devices_specs/" with the downloaded one (feel free to save the original file somewhere)</li>
  <li>In the SavedGames DCS directory make a folder called PersistentAbris, inside it a folder call ABRIS, and inside it a folder called Database.<br>
      You should end up with folder structure inside the SavedGames directory: PersistentAbris/ABRIS/Database </li>
  <br>
  Those are the bare minimum steps to get PersistentAbris working, you should be able to save and load you data now. <br>
  <b>You can find information about saving and loading data in the "How to use" section below</b>
</ol>

<h3>PersistentAbrisManager method</h3>
<ol>
  <li></li>
  <li></li>
  <li></li>
</ol>

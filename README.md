<h1>Description</h1>
  PersistentAbris is a solution to the problem of losing all your routes, additional info, nav data and options in the Ka-50 when leaving a mission or server.
  
  The solution to making all the routes and map info persistent across missions is to modify the <code>ABRIS.lua</code> file, which is responsible for saving and loading said data, so that is saves all the data to a set of files in a location in the SavedGames DCS directory, where it will also read them from. From testing, this does not appear to break the integrity check, so you should be able to fly on any server.
  
>[!NOTE]
>Currently, if a mission has baked in abris data, your persistent files will not be loaded for that mission. I have tried a couple of ways of getting around this issue, but have yet to find a solution</b>
  
  With just the steps described above, you would have a single set of files containing all your routes, additional info and nav data, which would accumulate quite a collection given enough time. Given that you would probably want to avoid having a massive amount of routes and possibly conflicting or inaccurate map elements, I have developed a manager app to work alongside the modified ABRIS.lua file. Keep in mind that you do not need the manager app for the persistent data to work, only to manage what you load and save in an easier fassion.

<h1>Installation</h1>
As said before, you will need to do two things to make PersistentAbris work: overwrite the <code>ABRIS.lua</code> file with the modified version and make a certain folder structure inside the SavedGames DCS directory.

There are two ways of doing this:
<ol>
  <li>Manually (Mod only installation, no manager app)</li>
  <li>Via the manager app (Recommended)</li>
</ol>

<h32>Manual method</h3>
<ol>
  <li>Download the modified <code>ABRIS.lua</code> and <code>Options_example.lua</code> files from the repository above</li>
  <li>Repalce the original ABRIS.lua file in <code>[your dcs root directory]/Mods/aircraft/Ka-50_3/Cockpit/Scripts/Devices_specs/</code> with the downloaded one (feel free to save the original file somewhere)</li>
  <li>In the SavedGames DCS directory make a folder called <code>PersistentAbris</code>, inside it a folder called <code>ABRIS</code>, and inside it a folder called <code>Database</code>.<br>
      You should end up with this folder structure inside the SavedGames DCS directory: <code>PersistentAbris/ABRIS/Database</code></li>
  <li>Place the <code>Options_example.lua</code> inside the <code>PersistentAbris</code> folder.</li>
  <br>
  Those are the bare minimum steps to get PersistentAbris working, you should be able to save and load you data now. <br>
  <b>You can find information about saving and loading data in the <a href="#how-to-use">How to use</a> section below</b>
</ol>

<h3>PersistentAbrisManager method</h3>
<ol>
  <li>Download the lates release of the manager app (PersistentAbrisManager.zip)</li>
  <li>Unzip the downloaded archive directly into the <code>SavedGames/DCS/</code> directory</li>
  <li>Open the <code>PersistentAbris</code> folder that was created after unziping and launch <code>PersistentAbrisManager.exe</code></li>
  <li>To replace the <code>ABRIS.lua</code> file, we will focus on the bottom left section of the app titled: DCS root directory 
      <br><br>
      <img witdh="40%" src="./readme_data/pam_window_first_opening.png"></img>
      <br><br>
      Press the <code>Select Directory</code> button.<br>
      This will bring up a folder seletion interface. Simply navigate to the root directory of your DCS instalation ( The folder you select will likely be called <code>DCS World</code> )<br>
      After doing so, providing you selected the correct folder, the text box below the button should be populated with the full path to the folder in which <code>ABRIS.lua</code> is located.<br>
      The full path won't fit inside the allocated display space, but if it is showing a path, then it is the correct one as the app checks if the path exists.
      <br><br>
        <img witdh="40%" src="./readme_data/pam_window_selected_path.png"></img>
      <br><br>
      If the path is valid, it will also be saved in a .txt file inside the PersistentAbris directory and it will be loaded from there on any future launches of the manager app
  </li>
  <li>
      Having slected the path, press the <code>Replace ABRIS.lua</code> button.<br>
      It will create a copy of the <code>ABRIS.lua</code> file in the same directory it was found in (it will be renamed to <code>ABRIS_old.lua</code>) and copy the modified file in its place.<br>
    </li>
</ol>

>[!NOTE]
>The <code>ABRIS_old.lua</code> will not be overwritten if it already exists. If ED updates the <code>ABRIS.lua</code> file at some point, you will need to delete the <code>ABRIS_old.lua</code> to make sure it gets backed up when replacing the file again.

<h1>Updating the mod and app</h1>
If you are using only the modded <code>ABRIS.lua</code> file, you will need to replace it with the updated version (same with the <code>Options_example.lua</code> file)
<br>
If you are using the PersistentAbrisManager, you will need to download the new release and extract the zipped files directly in the <code>SavedGames/DCS</code> directory, the same way as in the installation process. All your data will remain saved, so be sure to allow the extraction process to overwrite any files it asks you to. 
<br><br>

>[!IMPORTANT]
>It is likely that any DCS updates will revert the modded <code>ABRIS.lua</code> file back to the vanila version, so be sure to replace the file after every update
  
<h3>How to use</h3>
<h3>Saving routes, additional info and nav data</h3>

>[!IMPORTANT]
>To save any routes in game, you will first need to save and name them using the PLAN page of the Abris.

  <ol>
    <li>Navigate to the <code>MENU/CONTROL/DTB</code> page of the abris.
        <br><br>
        <img width="25%" src="./readme_data/abris_dtb_page.png"></img>
        <br><br>
    </li>
    <li>Press the SAVE button and use the rotary knob or the arrow buttons to navigate to the data you want to save.<br>
        <ul>  
          <li>Pressing SAVE on NAVIGATIONAL DATA will save navigation points and map objects and other navigation information</li> 
          <li>Pressing SAVE on ADDITIONAL INFO will save Point and Line objects entered by user</li> 
          <li>Pressing SAVE on ROUTES will save routes entered by user</li>
        </ul>
    </li>
  </ol>
  The mentioned data will be stored into corresponding files inside the ABRIS/Database directory:
  <ul>
      <li>ROUTES.lua</li>
      <li>ADDITIONAL.lua</li>
      <li>NAVIGATION.lua</li>
    </ul>
      
>[!IMPORTANT]
><b>Keep in mind -</b> from testing it seems that the NAVIGATION.lua needs to go along with routes and additional info. Meaning, if you save either the routes or add. info, you need to save the navigatinal data along side them for them to work properly!<br>

>[!NOTE]
>The DTB page of the Abris has a use in vanila DCS as well, though not many people seem to know that. You can save all the mentioned data while in a mission or server, in the sense that when you die or respawn in that mission, the data doesn't get lost. It just doesn't provide the ability for that data to persist across missions, so reloading the mission or leaving the server would delete the data. The mod only builds on that system to make it persistant, which is why saving and loading of data can be done entierly in game.</b>

<h3>Saving Abris options</h3>
Currently, there is no way to save Abris options in game, so you have to manually edit a <code>Options.lua</code> file to do so and place it inside the <code>Database</code> folder so it can be loaded in game.
<br>
If you followed the <a href="#installation">installation guide</a>, you will have a <code>Options_example.lua</code> inside the <code>PersistentAbris</code> directory. You can copy it to the database folder and rename it to <code>Options.lua</code>
  
<h3>Loading data in game</h3>
  The loading of the data is automatic.<br>
  When you spawn in a Ka-50, the data stored in the "ABRIS/Database" folder will be loaded into the Abris.<br>
  With that in mind, you can change the data you have loaded in your abris during a mission by respawning. This is achived by moving the wanted data files into the Database folder.<br><br>

<h3>PersistentAbrisManager</h3>
  <img witdh="40%" src="./readme_data/pam_window_with_collections.png"></img><br>
  We will analyse all aspects of the manager app, apart from the "DCS root directory" section, as it was covered in the installation process.<br>

  <h4>Working principle of the app</h4>
    The manager is designed to allow you to easily make different collections of Abris data.<br>
    The data consists of the 4 files mentioned in the Saving section above.<br>
    By moving those files in and out of the <code>ABRIS/Database folder</code>, they can be loaded in game or stored in a different directory for later use.
    All the app does is it creates collections which consist of the abris data files by way of making folders in the <code>ABRIS/</code> directory and copying files between those folders and the <code>Database</code> folder.<br>
    The collections don't have to contain all 4 files, but as mentioned earlier, always save and load the navigation data along with the routes and/or additional info!
    
  <h4>Collection name input field</h4>
    The collection name field is used to indicate which collection you want to work with.<br>
    By typing the name of a collection that does not exist in this field, you will be able to create a collection with that name.<br>
    By typing the name of a collection that does exist, you will be able to modify it, load data from it, delete data from it or delete the collection itself.<br>
    Trying to type "Database" into the input field, the field will get cleared of all input as modifing the Database in that way would cause problems.

  <h4>Database Files</h4>
    This section consists of 4 check boxes which let you choose which files you want to manipulate.

  <h4>Collection and DTB control buttons</h4>
    This sections consists of 5 buttons used to manipulate the Database and the collections:<br>
      <ul>
        <li>
          <b>Create</b><br>
          This button allows you to create a collection with the name inserted into the "Collection Name" field.<br>
          To create a collection, it will copy files from the Database folder into a folder with the same name as the collection.<br>
          The check boxes will determine which files get copied to the collection.<br><br>
          In case that the name of a collection that already exists is input into the "Collection Name" field, the button will read "Update" instead of "Create".<br>
          The functionality will remain identical, the press of the button will move selected files from the Database folder into the corresponding collection folder.<br>
          Keep in mind that updating a collection with new files will override the files currently in it.
        </li><br>
        <li>
          <b>Delete</b><br>
          This button allows you to delete files from collections, or to delete collections themselves.<br>
          Choosing which collection to delete from is done via the "Collection Name" field. If the name entered into said field isn't a existing collection, nothing will happen upon clicking the button.
          In case that a collection has files in itself, the delete function will delete files from the collection.<br>
          The check boxes determine which files get deleted.<br><br>
          In case that the collection is empty, pressing the Delete button will delete the collection.<br>
          The check boxes are irrelevant in this case
        </li><br>
        <li>
          <b>Load</b><br>
          This button copies files from the selected collection into the Database folder.<br>
          The check boxes determine which files get loaded.<br>
          Any loaded files will overwrite the files in the Database folder, destroying any unsaved data.<br>
          This button will do nothing if the selected database does not exist or is empty
        </li><br>
        <li>
          <b>Clear</b><br>
          This button deletes files from the Database folder.<br>
          The check boxes determine which files get deleted.<br>
        </li><br>
        <li>
          <b>Refresh</b><br>
          This button refreshes the Collections display on the right side of the app. Only needed if manualy editing the files or folder structure.
        </li>
      </ul>
      
  <h4>Collections display</h4>
    This sections displays all the collections, along side the Database, and shows which files they contain within them.<br>
    <ul>
        <li>R -> Routes</li>
        <li>A -> Additional Info</li>
        <li>N -> Navigation Data</li>
        <li>O -> Options</li>
    </ul>
    A '+' indicates that the corresponding file exists and a '-' indicates that the file does not exist within the collection/database.<br>
    Double clicking on any of the collections within the display will copy their name to the "Collection Name" input field

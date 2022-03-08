# Steam Profile Commenter

Using this script you can bulk-comment on as much profiles as you need. The only thing you got to do is specifying your username, password, a list of profile urls (these must be the *full profile urls*, not just for example, the profile id), and a list of comments to make in the `config.json` file.

The comments will be made in the same order as you write them in the config file.

Be sure to also put a Chrome webdriver executable in the same directory as the cloned repository named `chromedriver.exe` otherwise it will not work. You can also modify the script to make it load the executable with whatever name you put on the directory, but in case the script is not working, either that is the problem or you downloaded a *webdriver* version that is different from your *actual browser*.

To run the script you need to have Python installed. I have tested it and it worked fine on version 3.8.10. You may also be able to run it on older/newer versions too. Since I have not used Windows in a long while, I do not remember how to invoke the python interpreter, but I'm going to assume it is with just ``python`` (I'm saying this because Windows and Linux have different ways). So, in order to make the initial setup, after having cloned the repository, open a terminal window in the same folder as the project is and start typing:

```
python -m pip install selenium
```

This will install the library required in order to comunicate with the browser. Then, assuming the library and its dependencies were correctly installed, run:

```
python application.py
```

This will start the bot. Now you just have to observe and wait.


## Remarks

You will most likely need to perform the Steam Guard verification every time you run the bot, so be prepared and have your phone near when you do so. When the prompt for the verification code appears just input it normaly and enter. From this point, I believe you can even input the code wrong a few times without the program crashing. If you take too long (precisely 10,000 seconds) the program will exit. 

And thats it! From here on the bot will make everything you specified in the config file. This might take a while depending on your internet and how much comments/profiles you are doing. This will also be quite anoying if you try to type or click on other windows whilst the bot is running due to technical reasons.
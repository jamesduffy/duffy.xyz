---
title: "Mac Setup 2019"
date: 2019-01-04T16:13:29-08:00
draft: false
toc: true
---

# Intro
This is a personal help document to that I use to get started on a new Mac. I occasionally come back to this to update it and make sure that my current settings are reflected here, but more often than not it gets updated the next time I setup a new mac.

<!--more-->

# Software
- 1Password
- Alfred
- Capture One 12
- Caret
- Choosy
- CleanMyMac 3
- Cyberduck
- DaisyDisk
- Docker
- Dropbox
- Firefox
- Google Play Music Desktop Player
- Google Chrome
- iTerm2
- Itsycal
- KeepingYouAwake
- Logitech Options
- Mountain Duck
- Rocket
- Synology Drive
- Fujifilm X Raw Studio

# Custom Settings
- Clock > Show seconds
- Disable Fast user switching in menu bar
- Turn off automatic brightness
- Turn display scaling to max
- Trackpad tracking speed to max
- Sound:  Uncheck user interface sound effects 
- Output:  Check: Show volume in menubar    
- Finder show folders before files
- Keyboard  Key repeat fastest Key delay until repeat (1 slower than fastest)  
- General > Appearance: Dark
- Default web browser: Choosy
- Dock Position: LeftEnable "Automatically hide and show the dock"
- Mission Control:Disable Automatically rearrange Spaces
- Security > General:Require password immediately after sleep
- Security > FileVault: On
- MouseScroll direction: NaturalTacking speed: Fastest
- Trackpad
  - Disable Look up & data detectorsSecondary click: bottom right cornerEnable "Silent clicking"
- AccessibilityDisplayEnable "Reduce transparency"

## Optional

### Disable Curly Quotes
If I had a dollar for every time I was trying to fix a programming issue and it ended up somehow Apple changed my quotes to curly quotes without my realizing it.

Go to System Preferences > Keyboard > Text > Uncheck "Use smart quotes and dashes"

# Development Environment

```
touch ~/.hushlogin

# Install Homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install brews
brew install python python@2 wget zsh-syntax-highlighting watch

# Install casks
brew cask install keepingyouawake android-file-transfer daisydisk tower alfred itsycal iterm2 sublime-text dropbox 1password tunnelblick slack caret keybase docker google-chrome firefox git htop

# Install oh-my-zsh
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

# Setup Firefox
1. Install Sidebar Tabs
2. Modify userChrome.css
   - Go to Hamburger menu --> Help --> Troubleshooting Information
   - Find the Profile Folder
   - In the profile folder create a folder called chrome
   - In that folder create a file called userChrome.css- Insert the following in the file:

```
#TabsToolbar {
    visibility: collapse !important;
}

#sidebar-box[sidebarcommand="treestyletab_piro_sakura_ne_jp-sidebar-action"] #sidebar-header {
  display: none;
}
```

3. Go to Hamburger menu --> Customize
   - Add Felixible space next to the back and forward buttons
   - Remove home button
   - Set:
     - Density: `Compact`
     - Theme: `Dark`


# Python

```
brew install python python3
pip install --user virtualenvwrapper
Add to .zshrc file
export PYTHONDONTWRITEBYTECODE=1
pip install flake8
```

# ZSH / iTerm2
- Set scrollback to unlimited
- Set history to 10,000
- Always show tabs
- Stretch tabs to fill tab bar
- Increase size of profile
- Colors: Solarized Dark


# Dock Applications
1. Finder
2. Calendar
3. Tweetbot
4. Todoist
5. Slack
6. Chrome
7. Firefox
8. Sublime Text
9. iTerm
10. Tower

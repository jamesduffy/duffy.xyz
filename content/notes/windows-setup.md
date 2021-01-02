---
title: "Windows Setup"
date: 2020-01-01T16:13:29-08:00
draft: false
toc: true
summary: "This is a personal help document to that I use to get started on a new Windows Machine. I occasionally come back to this to update it and make sure that my current settings are reflected here, but more often than not it gets updated the next time I setup a new machine."
---

> This page is a draft and has not actually been used for setup of a Windows machine yet

# Intro
This is a personal help document to that I use to get started on a new Windows Machine. I occasionally come back to this to update it and make sure that my current settings are reflected here, but more often than not it gets updated the next time I setup a new machine.

# Getting ready

## Creating bootable USB
I didn't have a Windows machine laying around to create a bootable USB to install Windows. What I had to do was use my Mac and I followed the steps listed [on this gist](https://gist.github.com/bmatcuk/fda5ab0fb127e9fd62eaf43e845a51c3).

## Install
Follow all of the setup instructions as part of the normal Windows install.

## Create a Local User Account Instead
If you have a computer with an Ethernet cable, unplug it. If you’re connected to Wi-Fi, disconnect.

After you do, try creating a Microsoft account and you’ll see a “Something went wrong” error message. You can then click “Skip” to skip the Microsoft account creation process.

Once you’ve skipped the Microsoft account creation, the old “Who’s going to use this PC?” screen will appear. You can now create an offline account and sign in to Windows 10 without a Microsoft account—the option was there all along.

## Settings

### Unhide File Extensions and Hidden Files
To make file extensions visible again, enter "file explorer options" in the Windows search box, select the View tab, and then uncheck "Hide Extensions for Known File Types." While you're at it, toggle "Show hidden files, folders and drives" to on and uncheck “hide protected operating system files” so you can see all your system files.

### Enable Dark Mode
Enable Dark Mode by navigating to Settings->Personalization->Colors  and selecting Dark under the "choose your color" header.

### Get Rid of the Useless Lock Screen
When your computer is locked (or first boots), by default, Windows 10 shows you a lock screen with the time, a wallpaper and maybe (if you allow) some notifications. If you use Windows Hello facial or fingerprint recognition, you can log in by staring at the screen or putting one of your digits on the scanner. But, if you use a password, you have to click to dismiss the lock screen before the OS will allow you to enter your credentials.

That's one extra, unnecessary click every single time you want to unlock your PC. To get rid of the annoying lock screen and save your tired fingers,open the registry editor and navigate to HKEY_LOCAL_Machine\SOFTWARE\Policies\Microsoft\Windows and create a new key called Personalization if it doesn't already exist. Within the Personalization key, create a DWORD (32-bit) value called NoLockScreen and set it to 1.

### Switch Default Browsers
To change your default browser, first make sure you have the new browser installed. Search for "default apps" in the Windows search box and click the top result. Scroll down to "web browser," click the Edge icon and choose the browser you want to use.

### Protect Your Privacy
Navigate to Settings->Privacy and toggle all the settings to off. These currently include four options: "Let apps use advertising ID, " "Let websites provide locally relevant content," "Let Windows track app launches" and "Show me suggested content."

### Enable System Protection / Restore Points
System Protection, the feature which creates restore points you can return to, may be off. Turn on System Protection by typing "restore point" into the search box, clicking the top result, selecting your boot drive (usually C drive) , hitting the Configure button and then toggling "Turn on system protection" to on. We recommend setting maximum disk space usage to at least 5GB. Also you'll want to click the "Create" button to set up your first restore point.

# Software
- [1Password](https://1password.com/downloads/windows/)
- [Capture One](https://www.captureone.com/en/account/download)
- [Adobe Lightroom Classic](https://creativecloud.adobe.com/apps/all/desktop)
- [Dropbox](https://www.dropbox.com/install)
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)
- [Google Chrome](https://www.google.com/chrome/)
- [Logitech Options](https://www.logitech.com/en-us/product/options)
- [Steam](https://store.steampowered.com/about/)
- [Fujifilm X Raw Studio](https://fujifilm-x.com/en-us/support/download/software/x-raw-studio/)
- [Tower](https://www.git-tower.com/windows)
- [Todoist](https://todoist.com/downloads/windows?lang=en)
- [Sublime Text 3](https://www.sublimetext.com/3)

## Optional

# Setup Firefox
1. Install Sidebar Tabs
2. Modify userChrome.css
   - Go to Hamburger menu --> Help --> Troubleshooting Information
   - Find the Profile Folder
   - In the profile folder create a folder called chrome
   - In that folder create a file called userChrome.css- Insert the following in the file:

```css
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


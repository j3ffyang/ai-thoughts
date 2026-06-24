# 'Immutable' Operating System Choosing Strategy

## Disclaimer and Background
- 1/4 century Linux user for entperise level software development and solution design
- Open Source veteran
- All personal experience and personal opinion, without any intensive offending. 
- No intension to choose one over another one to imply one is good and another bad
- Not a complete comparasion of distros, just my personal opinion
- The situation can be extremely various in different situation, such as work, gaming, security, development, etc
- Linux becomes my **only** operating system for both work and leisure. No Microsoft Windows at all. None in my sight!

## TL;DR - native Arch Linux Captures Me

## Brainstorming
- Since having been a 1/4 century Linux power user, I live with Linux for both work and leisure. Always enjoy trying and playing with various Linux, from enterprise Red Hat, to Debian and Fedora, to Manjaro and CachyOS. Eventually recent 3 years, completely switched to Arch Linux
- Installed and configured Nvidia 3/ 4 series GPU with Steam, running on native Arch Linux. Really satisfied and having fun

## Policy
- Rather than specifically installing a dedicated "immutable" OS, such as Bazzite or Fedora Silverblue, personally I would like to use Arch Linux and Debian LTS. Giving myself more control, along with considering security and stability
- Hate **bloatware** therefore philosophy 
- Keep simple OS

## Immutable Strategy
- LTS if using Debian distro, without having to have lots of bloatware from Ubuntu, such as Games and default shell or whatever. I want to choose my own shell and just keep single one as preference
- Manjaro: very simple installation and by default all drivers such as Nvidia drivers with auto-detected
- CachyOS to cover all necessary drivers for specific hardware GPU, with great tuning feature so the end user doesn't have to tune themselves. It's a ready-to-run OS for gaming
- SteamOS and BlendOS, are Arch based **immutable** distro. 
- I rather want to install, control and manage my own Linux, than 

## Arch Linux
- Recent 3 years, I'm sticky with Arch Linux as with default installation, there are only ~500 packages or less, if running `fastfetch`, you choose browser, even `fastfetch` command. This is slick, and what I want. Installing all necessary drivers of Nvidia, the total package would be around ~600 packages. 

### Utilities and Tools

This could be very personalized and specific and unique by different user(s)

### Gaming 

If including `steam`, it'd be less than 800 packages. 

### Multi-media: 

I would personally install multimedia: `gimp`, `imagemagick`, `vlc` and `darktable`.

### Development 

`java` and `python` only. No `go` nor `rust` whatever else. I use `nvim` so that would require lots of dependencies to install, mostly Python

### Conclusion (personal)

This configuration is valid across all my machines, 1 desktop with Nvidia 3070, 1 ROG laptop with Nvidia 4090 and 1 Dell XPS without any GPU. Totally with GPU chips, there are ~1,100 packages installed and ~1,000 without GPU

I wrote an automatic script to install all the necessary packages when having a new Linux, installed from *basic* configuration. I like to install whichever I need, rather than what I would've been given by default

Installing a dedicated "Immutable" system is not for me. Why? Because, as a power user, 

1. You'd know what to install. If you break it, you fix it
2. You learn and grow then gain experience 
3. Mostly like me, my common installed app or libraries/ drivers won't change for a while. That means, as long as it's been tested, you can rely on it _mostly_

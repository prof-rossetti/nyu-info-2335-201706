# Credits, Notes, and Reference

## Professor Rossetti's Previous Courses

  + [Internet Programming](https://github.com/prof-rossetti/southernct-csc-443-01-201701)
  + [Database Design and Applications](https://github.com/prof-rossetti/gwu-istm-4121-10-201509)
  + [Management Info Systems](https://github.com/prof-rossetti/gwu-badm-2301-11-201509)

## Related NYU Courses and Resources

  + [NYU Data-driven Decision-making](http://www.d3mprof.com/)
  + [NYU Data Bootcamp](https://github.com/NYUDataBootcamp)
  + [NYU Principles of Urban Informatics](https://github.com/fedhere/PUI2016_fb55)

## NYU Services and Resources

  + [NYU Software](http://www.nyu.edu/life/information-technology/getting-started/software.html)
  + [NYU Co-Op Laptop Loaning](http://www.nyu.edu/life/information-technology/locations-and-facilities/student-technology-centers/laguardia-co-op.html#Laptop)
  + [NYU Lynda](https://www.nyu.edu/lynda)
  + [NYU Classroom AV Services](https://nyu.service-now.com/servicelink/kb_search.do?id=KB0013493)
  + [NYU Faculty](https://www.nyu.edu/faculty.html)
  + [Adding TA Permissions in NYU Classes](https://nyu.service-now.com/servicelink/kb_search.do?id=KB0010347)
  + [NYU Classroom Reservations](https://virtualems.stern.nyu.edu/BrowseReservations.aspx)
  + [NYU Schools and Colleges](https://www.nyu.edu/academics/schools-and-colleges.html)

## NYU Stern MediaSite

NYU Classes configuration for instructors:

> Typically, once you request recordings and autoposting, the only other thing you need to do is set the Mediasite tab on your NYU Classes course site to visible via settings > tool order > mediasite. Recordings will show up in this tab a few weeks after you enter the request via virtual EMS.

## Screencasting

  + [Converting QuickTime screen recordings to GIF format](https://gist.github.com/dergachev/4627207)): `ffmpeg -i ~/Dropbox/Screenshares/YOUR_SCREENCAST.mov -pix_fmt rgb24 -r 10 -f gif - | gifsicle --optimize=3 --delay=3 > admin/YOUR_SCREENCAST.gif`
  + [Hiding all Folders on the Desktop](http://www.cultofmac.com/272595/quickly-hide-icons-desktop-os-x-tips/): `defaults write com.apple.finder CreateDesktop false && killall Finder`
  + Recording a screencast with audio (ALMOST, BUT NOT FULLY WORKING):
    + http://apple.stackexchange.com/a/213305/94120
    + https://www.cnet.com/how-to/record-your-computers-screen-with-audio-on-a-mac/
    + https://github.com/mattingalls/Soundflower/releases/tag/2.0b2

## Course Material

  + [Installing Python 3 using Homebrew](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/)
  + [Forcibly pulling from upstream remote](https://stackoverflow.com/a/9646323/670433)
  + [Debugging in Python](http://daguar.github.io/2014/06/05/just-dropped-in-interactive-coding-in-ruby-python-javascript/)
  + [Initializing new Pip Project](http://www.idiotinside.com/2015/05/10/python-auto-generate-requirements-txt/)
  + [Mapping Lists in Python 3 (different than Python 2)](https://stackoverflow.com/questions/1303347/getting-a-map-to-return-a-list-in-python-3-x)
  + [String Formatting](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
  + [Grouping a List of Dictionaries by Key](https://adiyatmubarak.wordpress.com/2015/10/05/group-list-of-dictionary-data-by-particular-key-in-python/)

> "The Instacart Online Grocery Shopping Dataset 2017", Accessed from https://www.instacart.com/datasets/grocery-shopping-2017 on 2017-07-01.

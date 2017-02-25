#Pirat3me0w
download nhentai manga
###Install
Pirat3me0w works on Python2.7, and do not support Python3.x yet  

Pirat3me0w depends on this third-party packages  

    BeautifulSoup>=3.2.1
    argparse>=1.2.1
    requests>=2.4.3
    threadpool>=1.3.2

You can install them as easy as run

    pip install -r requirements.txt

Then run

    python setup.py install


Open the nhentai.net and get the manga' url, Maybe like this

    https://nhentai.net/g/188909/

`188909` is the manga' id, you can download this manga within  

    piratemeow --id 188909

More usage, see next section.

###Usage  
-  --id 
an id list for example '--id 188909, 188891'
-  --threads
thread number that you want to download; Maximum is 10
-  --path
saved path; default current dir
-  --timeout
download timeout
-  --proxy
download proxy

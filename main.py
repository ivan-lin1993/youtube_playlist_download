from urllib.request import urlopen

from pytube import Playlist, YouTube


def main():
    pl = Playlist(
        "https://www.youtube.com/playlist?list=PLRMCcJc0sUzswmhLqeea-jc182XZuJCjU")

    urls = pl.parse_links()
    print(urls)
    for url in urls:
        print("Now Download.....http://youtube.com{}".format(url))
        try:
            yt = YouTube('http://youtube.com{}'.format(url))
            (yt.streams
                .filter(progressive=True, file_extension='mp4')
                .order_by('resolution')
                .desc()
                .first()
                .download('./music'))
        except:
            print("pass")
            pass


if __name__ == '__main__':
    main()

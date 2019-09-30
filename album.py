def make_album(artist, song, **kwargs):
    kwargs['artist'] = artist
    kwargs['song'] = song

    return kwargs


def send_alert(names):
    for name in names:
        print(f'Hello {name}, How are you!')

    

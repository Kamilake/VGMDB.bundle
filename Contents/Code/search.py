import vgmdb

def search_albums(results, media, lang):

    query = media.album

    if query is None:
        query = media.name

    if media.filename is not None:
        if media.filename.find("&&&&") != -1:
            if media.filename.find("$$$$") != -1:
                query = media.filename[(media.filename.find("&&&&"))+4:(media.filename.find("$$$$"))]

    if "-" in query :
        query = query.replace("- ","-").replace("-","- ")

    result = vgmdb.search_albums(query)

    if result is None:
        return

    s = 100
    for album in result:
        results.Append(MetadataSearchResult(
            id = album['link'].replace('album/', ''),
            name = album['titles']['en'],
            year = album['release_date'][0:4],
            score = s,
            lang = lang
        ))
        s = s - 1

def search_artists(results, media, lang):
    query = media.artist
    if query is None:
        query = media.name
    result = vgmdb.search_artists(query)

    if result is None:
        return

    s = 100
    for artist in result:
        results.Append(MetadataSearchResult(
            id = artist['link'].replace('artist/', ''),
            name = artist['names']['en'],
            score = s,
            lang = lang
        ))
        s = s - 1

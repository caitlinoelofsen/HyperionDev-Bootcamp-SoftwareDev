import xml.etree.ElementTree as ET

tree = ET.parse('movie.xml')
root = tree.getroot()

# Parse the XML file
favorite_count = 0
non_favorite_count = 0

# Iterate over each 'movie element
for movie in root.iter('movie'):

    # Check if movie is favorite
    if movie.get('favorite') == 'True':
        favorite_count += 1
    else:
        non_favorite_count += 1

    print('Movie:')

    # Iterate over each child of the movie element
    for child in movie:
        if child.tag == 'description':
            print(f'   {child.tag} {" ".join(child.itertext()).strip()}')
        else:
            # Only print the tag for other child elements 
            print(f'   {child.tag}')

print(f'Number of favorite movies: {favorite_count}')
print(f'Number of non-favorite movies: {non_favorite_count}')

'''
I used the following resources to complete this task:
https://tinyurl.com/43wr9w6d
https://tinyurl.com/77j363tr
'''

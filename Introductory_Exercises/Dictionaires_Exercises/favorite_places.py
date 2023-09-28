favorite_places = {
    'arthur': ['canada', 'greece', 'switzerland'],
    'maria': ['canada', 'ireland', 'south korea'],
    'gustavo': ['new york', 'london', 'portugal'],
    'joão': ['paris', 'miami', 'spain'],
}
for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{name.title()}'s favorite place is:")
        for place in places:
            print(f"\t{place.title()}")
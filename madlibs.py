name = input("enter a name: ")
a,b,c,d,e,f = input("enter 6 different body parts: ").split()
g,h = input("enter 2 different adjectives").split()
i,j,k,l,m,n,o,p = input("enter 8 different nouns").split()
adverb = input("enter an adverb")
exclamation = input("enter an exclamation")
q,r = input("enter 2 different verbs in the past tense").split()
verb = input("enter a verb")

def show():
    return f'''FUN IN A MUD SLIDE
    Whoosh! Troop Leader {name} went sliding. He landed { a } -first in { g } mud.
    "It’s okay", he called back to the { i }. I meant to do that. I was just trying to show you how much fun
    it is to go { adverb }.
    {exclamation} ! George { q }. He lay on his { b } and
    down in the mud { c }-first.
    { p }! Chris shouted It’s { h }-man to the rescue! He got on his { j }
    and { d }-first down the { k } and into the { l }.)
    Hey, George! Alex cried out. {verb} fast!
    George grinned as Alex threw a pile of { m } right at him. There was { m } in his
    { e }, in his { f }, and under his { n }. Some { m } had even { r } its way into his { o } and onto
    his { a }.'''

print(show())

# # This was really fun!
# # Reproducible activity from
# # George Brown, Class Clown: Trouble Magnet
# #  by Nancy Krulik
# # Reproducible activity from

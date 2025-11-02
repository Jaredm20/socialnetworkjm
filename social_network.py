class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network")

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person_name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person_name} is friends with: {', '.join(friend_names)}")


network = SocialNetwork()

network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()

#A graph is the ideal structure to represent a social network because it allows for a bidirectional connection between the people on the list. Their relationship is represented through the edges of the graph where as the people themselves are represented as nodes.
#Lists and trees are more one-direction meaning there is no bi-lateral relationship between the two nodes. If we were to make this program with a tree or list there would be a hierarchy in the structure, meaning there is one person above another. In this case since it's a social network, there is no hierarchy in relationship.
#A couplet things I noticed when building this program was that if you were to add a larger network, the print would be a lot slower than what is desired. However, with the size of the connections and nodes that are present there were no noticeable tradeoffs. As of right now, as stated before, there is no noticeable difference in speed when executing the program.
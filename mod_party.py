from mod_char import Character


class Party:
    def __init__(self) -> None:
        """
        Initializes the instance with an empty list for members.
        """
        self.members: list[Character] = []

    def add_member(self, member):
        """
        Adds a member to the party.

        Parameters:
            self (obj): The party object.
            member (obj): The member to be added to the party.

        Returns:
            str: A message confirming the addition of the member to the party.
        """
        self.members.append(member)
        return f"{member.name} has been added to the party."

    def remove_member(self, member):
        """
        Remove a member from the party.

        Parameters:
            member (object): The member to be removed from the party.

        Returns:
            str: A message indicating that the member has been removed from the party.
        """
        self.members.remove(member)
        return f"{member.name} has been removed from the party."

    def party_info(self):
        """
        Returns a string of the names of all the members in the party.
        """
        return ", ".join([member.name for member in self.members])


"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        formattedMember = {
            "id": self._generateId(),
            "first_name": member["first_name"],
            "last_name": self.last_name
        }
        self._members.append(formattedMember)
        # fill this method and update the return
        return self._members, 200

    def delete_member(self, id):
        # fill this method and update the return
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                nombre = self._members[position]["first_name"]
                self._members.pop(position)
                return f"Member with id {id}, and first name {nombre}, deleted", 200
        return f"Member with id {id} not found", 404

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == int(id):
                return member, 200

        return f"Member with id {id} not found", 404

    def update_member(self, id, member):
        # fill this method and update the return
        newName = member["first_name"]
        for member in self._members:
            if member["id"] == int(id):
                member["first_name"] = newName
                return member, 200

        return f"Member with id {id} not found", 404

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

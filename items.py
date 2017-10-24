#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Andrew Kroft
10/22/2014
DPWP - Section 01
Dynamic Site
'''
#print "Content-Type: text/html\n"
from math import *


#Defines our list of minecraft items, and methods for returning data about it
class ItemList(object):
    def __init__(self):
        self.__blocks = []
        self.__tools = []
        self.__armor = []

        #Create lists of all of our items
        #blocks include (id, name, stack_size, recipe, material, blast_resistance, luminance, hardness, special)
        self.__blocks.append(Block(0, 'Wood', 64, [None,None,None,None,None,None,None,None,None], 'Wood', 10, 0, 2, 'Cannot be crafted, only gathered from trees.'))
        self.__blocks.append(Block(1, 'Wood Planks', 64, [None,None,None,None,0,None,None,None,None], 'Wood', 15, 0, 2, 'Planks... Made of wood.'))
        self.__blocks.append(Block(2, 'Crafting Table', 64, [None,None,None,None,1,1,None,1,1], 'Wood', 12.5, 0, 2.5, 'Right click after being placed to craft items that need more than 4 squares.'))
        self.__blocks.append(Block(3, 'Chest', 64, [1,1,1,1,None,1,1,1,1], 'Wood', 12.5, 0, 2.5, 'Can be used by right clicking after being placed.'))
        self.__blocks.append(Block(4, 'Wood Door', 64, [1,1,None,1,1,None,1,1,None], 'Wood', 15, 0, 3, 'Can be opened by right clicking after being placed.'))
        self.__blocks.append(Block(5, 'Wood Fence', 64, [None,None,None,1,100,1,1,100,1], 'Wood', 15, 0, 2, 'Counts as being 1.5 blocks tall.'))
        self.__blocks.append(Block(6, 'Boat', 1, [None,None,None,1,None,1,1,1,1], 'Wood', 'n/a', 'n/a', 'n/a', 'Place it in water to get around quicker.'))
        self.__blocks.append(Block(7, 'Wooden Button', 64, [None,None,None,None,1,None,None,None,None], 'Wood', 2.5, 0, 0.5, 'Used to trigger adjacent redstone or redstone devices.'))
        self.__blocks.append(Block(8, 'Fence Gate', 64, [None,None,None,100,1,100,100,1,100], 'Wood', 15, 0, 2, 'After being placed, right click to open. Counts as being 1.5 blocks tall.'))
        self.__blocks.append(Block(9, 'Wood Pressure Plate', 64, [None,None,None,1,1,None,None,None,None], 'Wood', 2.5, 0, 0.5, 'Triggers nearby redstone when walked on.'))
        self.__blocks.append(Block(10, 'Sign', 16, [1,1,1,1,1,1,None,100,None], 'Wood', 5, 0, 1, 'Enter a message for the world to see!'))
        self.__blocks.append(Block(11, 'Wood Slab', 64, [None,None,None,1,1,1,None,None,None], 'Wood', 15, 0, 2, 'Used to lay down a half of a block of wood planks.'))
        self.__blocks.append(Block(12, 'Wood Stairs', 64, [None,None,1,None,1,1,1,1,1], 'Wood', 15, 0, 2, 'After being placed, players and monsters can reach higher grounds without jumping.'))
        self.__blocks.append(Block(13, 'Wood Trapdoor', 64, [None,None,None,1,1,1,1,1,1], 'Wood', 15, 0, 3, 'Can be placed to block vertical entry ways.  Right click after placing to open or close.'))
        self.__blocks.append(Block(14, 'Cobblestone', 64, [None,None,None,None,None,None,None,None,None], 'Stone', 30, 0, 2, 'Cannot be crafted, only gathered from mining stone.'))
        self.__blocks.append(Block(15, 'Cobblestone Wall', 64, [None,None,None,14,14,14,14,14,14], 'Stone', 30, 0, 2, 'Counts as being 1.5 blocks tall.'))
        self.__blocks.append(Block(16, 'Furnace', 64, [14,14,14,14,None,14,14,14,14], 'Stone', 17.5, 0, 3.5, 'Used for cooking things and smelting ores.'))
        self.__blocks.append(Block(17, 'Lever', 64, [None,None,None,None,100,None,None,14,None], 'Stone', 2.5, 0, 0.5, 'Right click after placing to toggle nearby redstone.'))
        self.__blocks.append(Block(18, 'Cobblestone Slab', 64, [None,None,None,14,14,14,None,None,None], 'Stone', 30, 0, 2, 'Used to lay down a half of a block of cobblestone.'))
        self.__blocks.append(Block(19, 'Cobblestone Stairs', 64, [None,None,14,None,14,14,14,14,14], 'Stone', 30, 0, 2, 'After being placed, players and monsters can reach higher grounds without jumping.'))
        self.__blocks.append(Block(20, 'Stone', 64, [None,None,None,None,None,None,None,None,None], 'Stone', 30, 0, 1.5, 'Cannot be crafted, only gathered from mining stone using silk touch, or cooking cobblestone in a furnace.'))
        self.__blocks.append(Block(21, 'Stone Slab', 64, [None,None,None,20,20,20,None,None,None], 'Stone', 30, 0, 2, 'Used to lay down a half of a block of smooth stone.'))
        self.__blocks.append(Block(22, 'Stone Bricks', 64, [None,None,None,None,20,20,None,20,20], 'Stone', 30, 0, 1.5, 'Creates pretty stone bricks.'))
        self.__blocks.append(Block(23, 'Stone Brick Slab', 64, [None,None,None,22,22,22,None,None,None], 'Stone', 30, 0, 2, 'Used to lay down a half of a block of stone bricks.'))
        self.__blocks.append(Block(24, 'Stone Brick Stairs', 64, [None,None,22,None,22,22,22,22,22], 'Stone', 30, 0, 2, 'After being placed, players and monsters can reach higher grounds without jumping.'))
        self.__blocks.append(Block(25, 'Wool', 64, [None,None,None,None,113,113,None,113,113], 'Wool', 4, 0, 0.8, 'Can be crafted with string, or retrieved by using sheers on sheep.'))
        self.__blocks.append(Block(26, 'Bed', 1, [None,None,None,25,25,25,1,1,1], 'Wood', 1, 0, 0.2, 'Used to sleep through the night. Sleeping in a bed will set that spot as the players new respawn point.'))
        self.__blocks.append(Block(27, 'Carpet', 64, [None,None,None,None,None,None,None,25,25], 'Wool', 0.5, 0, 0.1, 'Can be placed for decoration, and dyed for style.'))
        self.__blocks.append(Block(28, 'Painting', 64, [100,100,100,100,25,100,100,100,100], 'Wool', 0, 0, 0, 'Spruce the place up a bit with a painting.'))
        self.__blocks.append(Block(29, 'Coal Block', 64, [116,116,116,116,116,116,116,116,116], 'Coal', 30, 0, 5, 'Can be crafted to get your coal back. Good for saving space.  Can also be used in a furnace for burning a lot of stuff at once!'))
        self.__blocks.append(Block(30, 'Torch', 64, [None,None,None,None,116,None,None,100,None], 'Wood', 0, 14, 0, 'Used to light up the surrounding area.'))

        #tools include (id, name, stack_size, recipe, durability, damage, special)
        self.__tools.append(Tool(100, 'Stick', 64, [None,None,None,None,1,None,None,1,None], 'n/a', 1, 'Used for crafting.'))
        self.__tools.append(Tool(101, 'Wood Pickaxe', 1, [1,1,1,None,100,None,None,100,None], 60, 3, 'Used for breaking stone blocks.'))
        self.__tools.append(Tool(102, 'Wood Axe', 1, [1,1,None,1,100,None,None,100,None], 60, 4, 'Used for breaking wood blocks.'))
        self.__tools.append(Tool(103, 'Wood Sword', 1, [None,1,None,None,1,None,None,100,None], 60, 5, 'Used for attacking monsters!'))
        self.__tools.append(Tool(104, 'Wood Shovel', 1, [None,1,None,None,100,None,None,100,None], 60, 2, 'Used for breaking dirt and sand blocks.'))
        self.__tools.append(Tool(105, 'Wood Hoe', 1, [1,1,None,None,100,None,None,100,None], 60, 1, 'Used for creating farmland to plant crops on.'))
        self.__tools.append(Tool(106, 'Leather', 64, [None,None,None,None,None,None,None,None,None], 'n/a', 1, 'Used for crafting, collected from killing cows or horses or rarely by fishing.'))
        self.__tools.append(Tool(107, 'Bowl', 64, [None,None,None,1,None,1,None,1,None], 'n/a', 1, 'Used to create meals, including mushroom or rabbit stew.'))
        self.__tools.append(Tool(108, 'Stone Pickaxe', 1, [14,14,14,None,100,None,None,100,None], 132, 4, 'Used for breaking stone blocks.'))
        self.__tools.append(Tool(109, 'Stone Axe', 1, [14,14,None,14,100,None,None,100,None], 132, 5, 'Used for breaking wood blocks.'))
        self.__tools.append(Tool(110, 'Stone Sword', 1, [None,14,None,None,14,None,None,100,None], 132, 6, 'Used for attacking monsters!'))
        self.__tools.append(Tool(111, 'Stone Shovel', 1, [None,14,None,None,100,None,None,100,None], 132, 3, 'Used for breaking dirt and sand blocks.'))
        self.__tools.append(Tool(112, 'Stone Hoe', 1, [14,14,None,None,100,None,None,100,None], 132, 1, 'Used for creating farmland to plant crops on.'))
        self.__tools.append(Tool(113, 'String', 64, [None,None,None,None,None,None,None,None,None], 'n/a', 1, 'Cannot be crafted.  Can be found as drops from spiders, by cutting down cobwebs with a sword or sheers and some various other ways.'))
        self.__tools.append(Tool(114, 'Bow', 1, [None,100,113,100,None,113,None,100,113], 385, 9, 'Ranged attack weapon, uses up an arrow on use and cannot be used without an arrow.  Damage of 9 is on full charge, the longer the mouse click is held, the more charged the bow becomes.  Minimum damage is 1.'))
        self.__tools.append(Tool(115, 'Fishing Rod', 1, [None,None,100,None,100,113,100,None,113], 65, 1, 'Used for fishing, of course.  Can be used to catch fish, garbage or rare treasures.'))
        self.__tools.append(Tool(116, 'Coal', 64, [None,None,None,None,None,None,None,None,None], 'n/a', 1, 'Coal is collected by mining and is used for crafting and as fuel in a furnace.  Charcoal can be made by burning raw wood in a furnace, and is used for the same things as coal.'))
        self.__tools.append(Tool(117, 'Iron Ingot', 64, [None,None,None,None,None,None,None,None,None], 'n/a', 1, 'Used for crafting. Iron ingot is made by smelting down iron ore in a furnace.'))
        self.__tools.append(Tool(118, 'Gold Ingot', 64, [None,None,None,None,None,None,None,None,None], 'n/a', 1, 'Used for crafting. Gold ingot is made by smelting down gold ore in a furnace.'))
        self.__tools.append(Tool(119, 'Diamond', 64, [None,None,None,None,None,None,None,None,None], 'n/a', 1, 'Used for crafting. Diamond can only be found by mining deep under the surface.'))
        self.__tools.append(Tool(120, 'Gold Pickaxe', 1, [118,118,118,None,100,None,None,100,None], 33, 3, 'Used for breaking stone blocks.'))
        self.__tools.append(Tool(121, 'Gold Axe', 1, [118,118,None,118,100,None,None,100,None], 33, 4, 'Used for breaking wood blocks.'))
        self.__tools.append(Tool(122, 'Gold Sword', 1, [None,118,None,None,118,None,None,100,None], 33, 5, 'Used for attacking monsters!'))
        self.__tools.append(Tool(123, 'Gold Shovel', 1, [None,118,None,None,100,None,None,100,None], 33, 2, 'Used for breaking dirt and sand blocks.'))
        self.__tools.append(Tool(124, 'Gold Hoe', 1, [118,118,None,None,100,None,None,100,None], 33, 1, 'Used for creating farmland to plant crops on.'))
        self.__tools.append(Tool(125, 'Iron Pickaxe', 1, [117,117,117,None,100,None,None,100,None], 251, 5, 'Used for breaking stone blocks.'))
        self.__tools.append(Tool(126, 'Iron Axe', 1, [117,117,None,117,100,None,None,100,None], 251, 6, 'Used for breaking wood blocks.'))
        self.__tools.append(Tool(127, 'Iron Sword', 1, [None,117,None,None,117,None,None,100,None], 251, 7, 'Used for attacking monsters!'))
        self.__tools.append(Tool(128, 'Iron Shovel', 1, [None,117,None,None,100,None,None,100,None], 251, 4, 'Used for breaking dirt and sand blocks.'))
        self.__tools.append(Tool(129, 'Iron Hoe', 1, [117,117,None,None,100,None,None,100,None], 251, 1, 'Used for creating farmland to plant crops on.'))
        self.__tools.append(Tool(130, 'Diamond Pickaxe', 1, [119,119,119,None,100,None,None,100,None], 1562, 6, 'Used for breaking stone blocks.'))
        self.__tools.append(Tool(131, 'Diamond Axe', 1, [119,119,None,119,100,None,None,100,None], 1562, 7, 'Used for breaking wood blocks.'))
        self.__tools.append(Tool(132, 'Diamond Sword', 1, [None,119,None,None,119,None,None,100,None], 1562, 8, 'Used for attacking monsters!'))
        self.__tools.append(Tool(133, 'Diamond Shovel', 1, [None,119,None,None,100,None,None,100,None], 1562, 5, 'Used for breaking dirt and sand blocks.'))
        self.__tools.append(Tool(134, 'Diamond Hoe', 1, [119,119,None,None,100,None,None,100,None], 1562, 1, 'Used for creating farmland to plant crops on.'))

        #armor include (id, name, stack_size, recipe, durability, body_part, armor)
        self.__armor.append(Armor(200, 'Leather Helmet', 1, [105,105,105,105,None,105,None,None,None], 56, 'Head', 1))
        self.__armor.append(Armor(201, 'Leather Tunic', 1, [105,None,105,105,105,105,105,105,105], 81, 'Torso', 3))
        self.__armor.append(Armor(202, 'Leather Leggings', 1, [105,105,105,105,None,105,105,None,105], 76, 'Legs', 2))
        self.__armor.append(Armor(203, 'Leather Boots', 1, [None,None,None,105,None,105,105,None,105], 66, 'Feet', 1))
        self.__armor.append(Armor(204, 'Gold Helmet', 1, [118,118,118,118,None,118,None,None,None], 78, 'Head', 2))
        self.__armor.append(Armor(205, 'Gold Chestplate', 1, [118,None,118,118,118,118,118,118,118], 113, 'Torso', 5))
        self.__armor.append(Armor(206, 'Gold Leggings', 1, [118,118,118,118,None,118,118,None,118], 106, 'Legs', 3))
        self.__armor.append(Armor(207, 'Gold Boots', 1, [None,None,None,118,None,118,118,None,118], 92, 'Feet', 1))
        self.__armor.append(Armor(208, 'Iron Helmet', 1, [117,117,117,117,None,117,None,None,None], 166, 'Head', 2))
        self.__armor.append(Armor(209, 'Iron Breastplate', 1, [117,None,117,117,117,117,117,117,117], 241, 'Torso', 6))
        self.__armor.append(Armor(210, 'Iron Leggings', 1, [117,117,117,117,None,117,117,None,117], 226, 'Legs', 5))
        self.__armor.append(Armor(211, 'Iron Boots', 1, [None,None,None,117,None,117,117,None,117], 196, 'Feet', 2))
        self.__armor.append(Armor(212, 'Diamond Helmet', 1, [119,119,119,119,None,119,None,None,None], 364, 'Head', 3))
        self.__armor.append(Armor(213, 'Diamond Breastplate', 1, [119,None,119,119,119,119,119,119,119], 529, 'Torso', 8))
        self.__armor.append(Armor(214, 'Diamond Leggings', 1, [119,119,119,119,None,119,119,None,119], 496, 'Legs', 6))
        self.__armor.append(Armor(215, 'Diamond Boots', 1, [None,None,None,119,None,119,119,None,119], 430, 'Feet', 3))

    def display(self): #return all items on the home page
        #Set output variable to display placeable blocks
        output = '''
        <fieldset>
            <legend>Place-able Blocks</legend>
            '''
        #loop through to add all blocks to output
        for item in self.__blocks:
            output += item.button_display()
        #close out fieldset for blocks
        output += '''
        </fieldset>'''

        #add tools and items to the output variable
        output += '''
        <fieldset>
            <legend>Tools and Items</legend>
            '''
        #loop through to add all tools to output
        for item in self.__tools:
            output += item.button_display()
        #close out fieldset for tools
        output += '''
        </fieldset>'''

        #add armor to the output variable
        output += '''
        <fieldset>
            <legend>Armor</legend>
            '''
        #loop through to add all armor to output
        for item in self.__armor:
            output += item.button_display()
        #close out fieldset for armor
        output += '''
        </fieldset>'''

        return output


    def item_display(self, id): #return an individual item for display on the content page
        #Get the object we need from object_test method
        temp_object = self.object_test(id)
        #Return the item_display() information for displaying
        return temp_object.item_display()


    def recipe_display(self, id):  #send back a display for our recipe!
        #set our object so we can get the recipe
        temp_object = self.object_test(id)
        #create a temporary variable to for placing an "a" in front of non plural items
        a = 'a'
        if temp_object.name.endswith('s'):
            a = ''
        #set a temp variable for holding onto our string that will be returned to be displayed
        temp = """
            <h2>{temp_object.name}</h2>
            <p>
                Below is the crafting grid to make {a} {temp_object.name}.  Often the items simply need to follow the pattern
                but can be mirrored vertically or moved around in the grid.  Click any of the items in the grid to see how
                to craft it!
            </p>
            <div class='recipe'>
            """.format(**locals())

        #set up recipe list
        recipe = temp_object.get_recipe()

        #loop through the recipe and display them on the screen as clickable buttons, so the user can check out that
        #item as well
        #set variable x, when x%3 = 0 we have reached the end of the row and should add a break
        x=0

        #set variable empty to determine if all slots are empty
        #if they are all empty, we will display a message to note that the item is not able to be crafted
        empty=0

        for item in recipe:
            #if we don't have an empty square, then fill it in
            if item is not None:
                if int(item) >= 200:
                    temp += self.__armor[int(item)-200].button_display()
                elif int(item) >= 100:
                    temp += self.__tools[int(item)-100].button_display()
                else:
                    temp += self.__blocks[int(item)].button_display()
            else:
                temp += """
                <a class='item_icon'><button><img src='static/images/icon_blank.png' alt='item' /></button></a>
                """
                empty += 1
            x += 1

            if x%3 == 0:
                temp += '<br />'

        #Add a cool arrow to point form our recipe to our item
        temp += "</div><img src='static/images/arrow.png' alt='arrow' style='margin-left:50px;' />"
        if empty == 9:
          print("EMPTY")
          temp = """
          <h2>{temp_object.name}</h2>
          <p style='text-align:center;'>
            {temp_object.name} cannot be crafted!  You'll have to find it in the world.
          </p>
          <img src='static/images/empty.png' alt='empty' />
          """.format(**locals())
        return temp

    def object_test(self, id):
        #Test to find out which object we are looking for, then
        #id 0-99 is Block
        #id 100-199 is Tool
        #id 200-299 is Armor
        if int(id) >= 200:
            return self.__armor[int(id)-200]
        elif int(id) >= 100:
            return self.__tools[int(id)-100]
        else:
            return self.__blocks[int(id)]


#Superclass for our specific item classes of block, tool and armor
class Item(object):
    def __init__(self, id, name, stack_size, recipe):
        self._id = id
        self._name = name
        self._stack_size = stack_size
        self._recipe = recipe

    #send back info for displaying button on home screen
    def button_display(self):
        id = str(self._id)
        temp = """
        <a class='item_icon' href='.?id={self._id}'>
            <button>
            <img src='static/images/icon_{self._id}.png' alt='item' />
            </button><br />
            <span class='tooltip'>{self._name}</span>
        </a>
        """.format(**locals())

        return temp

    #send back info for displaying item details
    def item_display(self):
        id = str(self._id)
        name = str(self._name)
        stack_size = str(self._stack_size)

        temp = """
            <img src='static/images/image_{id}.png' alt='item' ?><br />
        """.format(**locals())

        return temp

    #create method for returning the list of our recipe
    def get_recipe(self):
        return self._recipe

    #Getter and setter for self._name
    @property
    def name(self):
        return self._name


#Sub-class to Item class to define a place-able block object
class Block(Item):
    def __init__(self, id, name, stack_size, recipe, material, blast_resistance, luminance, hardness, special):
        Item.__init__(self, id, name, stack_size, recipe)
        #set all variables based on input
        self.__material = material
        self.__blast_resistance = blast_resistance
        self.__luminance = luminance
        self.__hardness = hardness
        self.__special = special

    #send back info for displaying item details
    def item_display(self):
        id = str(self._id)
        name = str(self._name)
        stack_size = str(self._stack_size)
        material = str(self.__material)
        blast_resistance = str(self.__blast_resistance)
        luminance = str(self.__luminance)
        hardness = str(self.__hardness)
        special = str(self.__special)
        inventory_capacity = int(stack_size) * 36

        temp = """
            <img src='static/images/image_{id}.png' alt='item' ?><br />
            <ul>
                <li>Stack size: {stack_size}</li>
                <li>Can fit {inventory_capacity} in your inventory at once!</li>
                <li>Material: {material}</li>
                <li>Blast resistance: {blast_resistance}</li>
                <li>Luminance: {luminance}</li>
                <li>Hardness: {hardness}</li>
                <li>Special notes: {special}</li>
            </ul>
        """.format(**locals())

        return temp



#Sub-class to Item class to define a tool or weapon object
class Tool(Item):
    def __init__(self, id, name, stack_size, recipe, durability, damage, special):
        Item.__init__(self, id, name, stack_size, recipe)
        #set all variables based on input
        self.__durability = durability
        self.__damage = damage
        self.__special = special

    #send back info for displaying item details
    def item_display(self):
        id = str(self._id)
        name = str(self._name)
        stack_size = str(self._stack_size)
        durability = str(self.__durability)
        damage = str(self.__damage)
        special = str(self.__special)
        inventory_capacity = int(stack_size) * 36
        #Determine how many hits it would take to kill a zombie
        #This is based on A zombie having 4 armor, or 16% damage reduction and 20 hitpoints
        zombie_hits = int(ceil(20 / (int(damage) - int(damage) * .16)))

        temp = """
            <img src='static/images/image_{id}.png' alt='item' ?><br />
            <ul>
                <li>Stack size: {stack_size}</li>
                <li>Can fit {inventory_capacity} in your inventory at once!</li>
                <li>Durability: {durability}</li>
                <li>Damage: {damage}</li>
                <li>It will take {zombie_hits} hits to kill a zombie with this item.</li>
                <li>Special notes: {special}</li>
            </ul>
        """.format(**locals())

        return temp


#Sub-class to Item class to define an armor object
class Armor(Item):
    def __init__(self, id, name, stack_size, recipe, durability, body_part, armor):
        Item.__init__(self, id, name, stack_size, recipe)
        #set all variables based on input
        self.__durability = durability
        self.__body_part = body_part
        self.__armor = armor

    #send back info for displaying item details
    def item_display(self):
        id = str(self._id)
        name = str(self._name)
        stack_size = str(self._stack_size)
        durability = str(self.__durability)
        body_part = str(self.__body_part)
        armor = str(self.__armor)
        inventory_capacity = int(stack_size) * 36
        #calculate % damage reduction by using this item
        damage_reduction = int(armor) * 4

        temp = """
            <img src='static/images/image_{id}.png' alt='item' ?><br />
            <ul>
                <li>Stack size: {stack_size}</li>
                <li>Can fit {inventory_capacity} in your inventory at once!</li>
                <li>Durabilty: {durability}</li>
                <li>Body part: {body_part}</li>
                <li>Armor gained: {armor}</li>
                <li>Damage reduction granted: {damage_reduction}%</li>
            </ul>
        """.format(**locals())

        return temp

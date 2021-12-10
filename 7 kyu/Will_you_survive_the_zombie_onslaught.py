"""7 kyu
Will you survive the zombie onslaught?

I'm afraid you're in a rather unfortunate situation. You've injured your leg, and are unable to walk, and a number of
zombies are shuffling towards you, intent on eating your brains. Luckily, you're a crack shot, and have your trusty
rifle to hand.

The zombies start at range metres, and move at 0.5 metres per second. Each second, you first shoot one zombie, and then
the remaining zombies shamble forwards another 0.5 metres.

If any zombies manage to get to 0 metres, you get eaten. If you run out of ammo before shooting all the zombies, you'll
also get eaten. To keep things simple, we can ignore any time spent reloading.

Write a function that accepts the total number of zombies, a range in metres, and the number of bullets you have.

If you shoot all the zombies, return "You shot all X zombies." If you get eaten before killing all the zombies, and
before running out of ammo, return "You shot X zombies before being eaten: overwhelmed."

If you run out of ammo before shooting all the zombies, return "You shot X zombies before being eaten: ran out of ammo."
(If you run out of ammo at the same time as the remaining zombies reach you, return "You shot X zombies before being
eaten: overwhelmed.".)

Good luck! (I think you're going to need it.)
Fundamentals
Games"""


# How this works
def zombie_shootout(zombies, distance, ammo):
    if zombies == 0:
        print(f"You shot all {zombies} zombies.")

    j = distance
    c = 0
    for i in range(0, distance):
        distance = distance - 0.5
        diff = ammo - 1
        if diff >= 0:
            ammo = ammo - 1
            zombies = zombies - 1
            c = c + 1
        elif zombies == 0:
            print(f"You shot all {zombies}")
        else:
            distance = distance - 0.5

    if ammo == 0 and zombies >= 1 and j == 0.0:
        t = "overwhelmed."
    elif ammo == 0:
        t = "ran out of ammo."
    else:
        t = "overwhelmed"

    print(f"You shot {c} zombies before being eaten: {t}")

    # zombie = zombies
    # shot = 0
    # for i in range(0, ammo):
    #     if ammo >= 0:
    #         zombie = zombie - 1
    #         distance = distance - 0.5
    #         ammo = ammo - 1
    #         shot = shot+1
    #         if zombie == 0 and distance > 0 and ammo > 0:
    #             print(f"You shot all {shot} zombies.")
    #         elif zombie > 0 and ammo > 0 and distance == 0:
    #             print(f"You shot {shot} zombies before being eaten: overwhelmed.")
    #         elif zombie > 0 and ammo == 0 and distance > 0:
    #             print(f"You shot {shot} zombies before being eaten: ran out of ammo.")
    #         elif zombie == 0 and ammo == 0 and distance > 0:
    #             print(f"You shot {shot} zombies before being eaten: overwhelmed.")


zombie_shootout(3, 10, 10)
zombie_shootout(100, 8, 200)
zombie_shootout(50, 10, 8)

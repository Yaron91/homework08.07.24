vol_level: (int) = int (input ("Enter the volume level between 0-10: "));
match vol_level:
    case 0:
        print ("Mute");
    case 1 | 2:
        print ("Very Quiet")
    case 3:
        print ("Quiet");
    case 4:
        print ("Moderately Quiet");
    case 5:
        print ("Medium")
    case 6:
        print ("Moderately Loud");
    case 7:
        print ("Loud");
    case 8:
        print ("Very Loud");
    case 9 | 10:
        print ("Extremely Loud");
    case _:
        print ("Write the correct number!");

try:
    x = float('abc123')
    print(x)
    except IOError:
        print('This code caused an IOError.')
    except ZeroDivisionError:
        print('This code caused a ZeroDivisionError.')
    except:
        print('An error happened.')
        print('The end.')
import time
import random


strength = {'name': 10, 'surname': 20, 'nickname': 30, 'alias': 40, 'aka': 50}

gk_questions = [
    {"In what year did the Byzantine Empire officially fall?": "1453"},
    {"What is the chemical symbol for the element Tungsten?": "w"},
    {"Who wrote the 17th-century epic poem Paradise Lost?": "john milton"},
    {"What is the deepest known oceanic trench on Earth?": "mariana trench"}
]


def short_form(idx, *names, **addons):
    final = ''
    try:
        
        for name in names:
            final = final + name[idx]
        
        
        for keys in addons:
            if keys == 'prefix':
                final = addons[keys] + final
            elif keys == 'suffix':
                final = final + addons[keys]
            else:
                print('You are not good at typing, are you ...')
                
    except TypeError as e:
        print('Wrong data type: ', e)
    except IndexError as e:
        print('Indexing is going wrong:', e)
    except Exception as e:
        print('Something went wrong', e)
    else:
        return final
    finally:
        print("Hope you managed to pass this stage ...")


def name_strength(**fullname):
    result = 0
    try:
        for key, value in fullname.items():
            result += strength[key] * len(value)
    except KeyError as e:
        print('Perhaps you are giving too many fields', e)
    else: 
        return result



def agent_report(codename, score):
    print("\n--- AGENT ID BADGE ---")
    agent_info = {"Codename": codename, "Strength Score": score, "Status": "Active"} 
    
    for key, value in agent_info.items():
        print(f"{key}: {value}")
    print("----------------------\n")



def validate(**prelimdata):
    try:
        assert prelimdata['sc'] != None
        assert prelimdata['ns'] != None
    except KeyError as e:
        print('You are really bad at typing, aren\'t you?')
        print('Validation failed due to ', e)
    except AssertionError:
        print('One of the earlier steps has gone wrong.')
        print('Validation failed')
    else:
        print('Looking good so far ...')
        print('Sending for deeper validation')
        print('opening connection to a remote server ...')
        try:
            deep_validate(prelimdata)
        except ValueError:
            print('There is something deeply wrong')
            print('Validation failed ...')
            
            # --- GK Challenge Fallback ---
            print('\n--- LUCK CHECK FAILED: GK CHALLENGE ---')
            selected_dict = random.choice(gk_questions)
            question_key = list(selected_dict.keys())[0]
            correct_answer = selected_dict[question_key]
            
            user_answer = input(f"Answer this GK question to enter anyway: {question_key} ").strip().lower()
            
            if user_answer == correct_answer:
                print('Congrats ... GK Challenge Successful!')
                print('Welcome to my world!')
            else:
                print('GK Challenge Failed. Sorry, validation fully unsuccessful.')
        else:
            print('Congrats ... Validation Successful')
            print('Welcome to my world!')
        finally:
            print('Closing connection to the remote server')


def deep_validate(prelimdata):
    print(prelimdata)

    
    threshold_ns = random.randint(50, 1500)
    threshold_sc = random.randint(10, 50)

    print()
    print(threshold_ns, threshold_sc)
    print()
    
    # If your score is too high, it triggers an error
    if prelimdata['ns'] > threshold_ns or len(prelimdata['sc']) > threshold_sc:
        raise ValueError



print('Welcome to the Programmers\' Den')
print("I hear you have been learning Python")
print('Guess you can use the command line to create your own welcome kit\n')

print('The process is simple, create a short code, check your name strength and then validate\n')

print('For short code, use: sc = short_form(idx, a few words about yourself, prefix=..., suffix=...)')
print('For name strength code, use: ns = name_strength(name=..., aka=...)')
print('For your Agent ID Badge , use: agent_report(sc, ns)')
print('For validate, use: validate(sc=sc, ns=ns)\n')

print('Alright champ, get going ...')
print(' ')

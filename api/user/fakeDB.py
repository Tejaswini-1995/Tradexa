from ..post.models import Post
from ..user.models import CustomUserModel
import random
import datetime

users = [
    {"email": "xhyojun.lee.773@dilayda.com", "isFake": True},
    {"email": "oechslin@me.com", "isFake": True},
    {"email": "zwood@live.com", "isFake": True},
    {"email": "bastian@hotmail.com", "isFake": True},
    {"email": "cparis@sbcglobal.net", "isFake": True},
    {"email": "kdawson@aol.com", "isFake": True},
    {"email": "mwilson@sbcglobal.net", "isFake": True},
    {"email": "manuals@aol.com", "isFake": True},
    {"email": "jeffcovey@optonline.net", "isFake": True},
    {"email": "geeber@mac.com", "isFake": True},
    {"email": "kiddailey@msn.com", "isFake": True},
    {"email": "shin.lee.773@dilayda.com", "isFake": True},
    {"email": "malvar@hotmail.com", "isFake": True},
    {"email": "pappp@hotmail.com", "isFake": True},
    {"email": "esbeck@yahoo.ca", "isFake": True},
    {"email": "storerm@outlook.com", "isFake": True},
    {"email": "bartak@optonline.net", "isFake": True},
    {"email": "mschilli@outlook.com", "isFake": True},
    {"email": "morain@yahoo.com", "isFake": True},
    {"email": "gknauss@gmail.com", "isFake": True},
    {"email": "mailarc@mac.com", "isFake": True},
    {"email": "itstatus@live.com", "isFake": True},
    {"email": "gumpish@outlook.com", "isFake": True},
    {"email": "mrsam@icloud.com", "isFake": True},
    {"email": "gilmoure@gmail.com", "isFake": True},
    {"email": "sisyphus@sbcglobal.net", "isFake": True},
    {"email": "ranasta@optonline.net", "isFake": True},
    {"email": "pjacklam@me.com", "isFake": True},
    {"email": "cgarcdia@icloud.com", "isFake": True},
    {"email": "cwwgarceria@icloud.com", "isFake": True},
    {"email": "knorr@sbcglobal.net", "isFake": True},
    {"email": "atmarks@att.net", "isFake": True},
    {"email": "studyabr@mac.com", "isFake": True},
    {"email": "valdez@outlook.com", "isFake": True},
    {"email": "dkeeler@outlook.com", "isFake": True},
    {"email": "houle@gmail.com", "isFake": True},
    {"email": "andrewik@me.com", "isFake": True},
    {"email": "sjava@icloud.com", "isFake": True},
    {"email": "wainwrig@msn.com", "isFake": True},
    {"email": "skythe@gmail.com", "isFake": True},
    {"email": "cparis@msn.com", "isFake": True},
    {"email": "mhouston@att.net", "isFake": True},
    {"email": "ducasse@msn.com", "isFake": True},
    {"email": "jschauma@yahoo.ca", "isFake": True},
    {"email": "danneng@optonline.net", "isFake": True},
    {"email": "tattooman@mac.com", "isFake": True},
    {"email": "retoh@aol.com", "isFake": True},
    {"email": "barnett@verizon.net", "isFake": True},
    {"email": "kourai@att.nett", "isFake": True},
    {"email": "sartak@yahoo.ca", "isFake": True},
    {"email": "natepuri@msn.com", "isFake": True},
    {"email": "kingjoshi@me.com", "isFake": True},
    {"email": "peterhoeg@att.net", "isFake": True},
    {"email": "zilla@live.com", "isFake": True},
]

posts = [
    {
        "post_content": "I'm really excited to get into the app! Anyone have any suggestions?",
        "post_title": "Montgomery, Alabama",
        "post_state": "Alabama",
        "post_city": "",
    },
    {
        "post_content": "Quarantine has been super difficult to manage and I feel like I don't know where to start. I am posting, hoping someone can help!",
        "post_title": "Juneau, Alaska",
        "post_state": "Alaska",
        "post_city": "",
    },
    {
        "post_content": "Anyone know a good resource for anxiety that I can save?",
        "post_title": "Tuscon, Arizona",
        "post_state": "Arizona",
        "post_city": "",
    },
    {
        "post_content": "I'm really excited to get into the app! Anyone have any suggestions?",
        "post_title": "Montgomery, Alabama",
        "post_state": "Alabama",
        "post_city": "",
    },
    {
        "post_content": "Honestly, I wish mental health was talked about more often. There is way too much stigma.",
        "post_title": "Hot Springs, Arkansas",
        "post_state": "Arkansas",
        "post_city": "",
    },
    {
        "post_content": "I really miss interacting with others and covid has made it so hard. What should I do to feel more connected?",
        "post_title": "Irvine, California",
        "post_state": "California",
        "post_city": "",
    },
    {
        "post_content": "Hi ya'll! This is my first post. Love this app. Anyone have advice on the most helpful mental health podcasts to get rid of anxiety?",
        "post_title": "Los Angeles, California",
        "post_state": "California",
        "post_city": "",
    },
    {
        "post_content": "Does anyone know if Diall works offline?",
        "post_title": "Boulder, Colorado",
        "post_state": "Colorado",
        "post_city": "",
    },
    {
        "post_content": "It was tough for me to start seeing a therapist, but when I started it was so much easier than I thought it would be. And when i'm not there, i love the resources section here.",
        "post_title": "New Haven, Connecticut",
        "post_state": "Connecticut",
        "post_city": "",
    },
    {
        "post_content": " When i clicked the domestic violence button, I was really scared, but I really want to say that it was SO easy! If anyone wants to talk about their experience, reply to this comment!",
        "post_title": "Dover, Delaware",
        "post_state": "Delaware",
        "post_city": "",
    },
    {
        "post_content": "Anyone know any good books or podcasts on vulnerability?",
        "post_title": "Miami, Florida",
        "post_state": "Florida",
        "post_city": "",
    },
    {
        "post_content": "Meditation changed my life and I have been incorporating a lot of different techniques into my daily life. Always down to learn more. ",
        "post_title": "Atlanta, Georgia",
        "post_state": "Georgia",
        "post_city": "",
    },
    {
        "post_content": "If you're reading this, you're enough! Pass along the kindness!",
        "post_title": "Honolulu, Hawaii",
        "post_state": "Hawaii",
        "post_city": "",
    },
    {
        "post_content": "My husband and I were experiencing a rocky patch not too long ago and finally decided to download this app to learn more about what we can do. What are the best therapy apps that actually work?",
        "post_title": "Boise, Idaho",
        "post_state": "Idaho",
        "post_city": "",
    },
    {
        "post_content": "Any other ED survivors here",
        "post_title": "Chicago, Illinois",
        "post_state": "Illinois",
        "post_city": "",
    },
    {
        "post_content": "The alliance for eating disorders was AMAZING at referring support for my daughter. If you need help, check them out!!",
        "post_title": "Bloomington, Indiana",
        "post_state": "Indiana",
        "post_city": "",
    },
    {
        "post_content": "Does hypnotherapy help repressed memories?",
        "post_title": "Des Moines, Iowa",
        "post_state": "Iowa",
        "post_city": "",
    },
    {
        "post_content": "How do you help someone that doesn't want to admit they need help?",
        "post_title": "Wichita, Kansas",
        "post_state": "Kansas",
        "post_city": "",
    },
    {
        "post_content": "Is it just me, or is it really hard to want to do anything when you feel depressed?",
        "post_title": "Louisville, Kentucky",
        "post_state": "Kentucky",
        "post_city": "",
    },
    {
        "post_content": "Does anyone think TikTok and social media is toxic orrrrr is it just me?",
        "post_title": "New Orleans, Louisiana",
        "post_state": "Louisiana",
        "post_city": "",
    },
    {
        "post_content": "SOOO my ex-boyfriend won't stop messaging me. What should I do?",
        "post_title": "Portland, Maine",
        "post_state": "Maine",
        "post_city": "",
    },
    {
        "post_content": "If I have an eating disorder, can I recover?",
        "post_title": "Baltimore, Maryland",
        "post_state": "Maryland",
        "post_city": "",
    },
    {
        "post_content": "Has anyone had a bad experience being on anti-anxiety meds? I have been feeling numb and I am going to speak to my doctor, but i want to know.",
        "post_title": "Boston, Massachusetts",
        "post_state": "Massachusetts",
        "post_city": "",
    },
    {
        "post_content": "This app is the not toxic side of social media. Thank god haha",
        "post_title": "Cambridge, Massachusetts",
        "post_state": "Massachusetts",
        "post_city": "",
    },
    {
        "post_content": "Ever since zoom classes started I lost all motivation and really miss seeing my friends. What should i do?",
        "post_title": "Ann Arbor, Michigan",
        "post_state": "Michigan",
        "post_city": "",
    },
    {
        "post_content": " I was near the walker art center and saw someone panicking and crying near the sculpture garden. I swear if i didn't have this app I would have had no idea who to call. Anyone else feel the same way?",
        "post_title": "Wayzata, Minnesota",
        "post_state": "Minnesota",
        "post_city": "",
    },
    {
        "post_content": "How can i get help paying for my medication?",
        "post_title": "Minnetonka, Minnesota",
        "post_state": "Minnesota",
        "post_city": "",
    },
    {
        "post_content": " I am burned out at work and want to leave. Anyone tried getting a life coach rather than a therapist?",
        "post_title": "Tupelo, Mississippi",
        "post_state": "Mississippi",
        "post_city": "",
    },
    {
        "post_content": " What's a good movie to watch with my kids to teach them about vulnerability?",
        "post_title": "Springfield, Missouri",
        "post_state": "Missouri",
        "post_city": "",
    },
    {
        "post_content": "Lol I heard Charli and Dixie were on this app?",
        "post_title": " Big Sky, Montana",
        "post_state": "Montana",
        "post_city": "",
    },
    {
        "post_content": "This app is like Instagram for mental health.",
        "post_title": "Lincoln, Nebraska",
        "post_state": "Nebraska",
        "post_city": "",
    },
    {
        "post_content": "COVID has been so tough but also brought so many positive things. The question is... when can we travel again!",
        "post_title": "Las Vegas, Nevada",
        "post_state": "Nevada",
        "post_city": "",
    },
    {
        "post_content": "I started on youtube and ended up here haha.",
        "post_title": "Concord, New Hampshire",
        "post_state": "New Hampshire",
        "post_city": "",
    },
    {
        "post_content": "Anyone have any tips for setting boundaries during work from home?",
        "post_title": "Hackettstown, New Jersey",
        "post_state": "New Jersey",
        "post_city": "",
    },
    {
        "post_content": "I am posting for a friend. What's the best way to join an AA group?",
        "post_title": "Albuquerque, New Mexico",
        "post_state": "New Mexico",
        "post_city": "",
    },
    {
        "post_content": "Just wanted to say that if the person you find isn't giving you the kind of support you need, look for another support option that is better for you and your needs. You deserve it.",
        "post_title": "New York City, New York",
        "post_state": "New York",
        "post_city": "",
    },
    {
        "post_content": "So I just came out to my best friend and he was super supportive, bt i am terrified to come out to my parents. Any advice?",
        "post_title": "Ogden, North Carolina",
        "post_state": "North Carolina",
        "post_city": "",
    },
    {
        "post_content": "Seasonal depression is real. It has been so cold here and I am losing my mind.",
        "post_title": "Fargo, North Dakota",
        "post_state": "North Dakota",
        "post_city": "",
    },
    {
        "post_content": "Has anyone ever texted the Crisis Text Line before?",
        "post_title": "Akron, Ohio",
        "post_state": "Ohio",
        "post_city": "",
    },
    {
        "post_content": "Ever since I started going on daily runs, I have been feeling a million times better. 10/10 recommend trying it during quarantine.",
        "post_title": "Tulsa, Oklahoma",
        "post_state": "Oklahoma",
        "post_city": "",
    },
    {
        "post_content": "As someone overwhelmed by parenthood, a competitive career, personal finances, without any family or close friends in the same state, this app is amazing.",
        "post_title": "Portland, Oregon",
        "post_state": "Oregon",
        "post_city": "",
    },
    {
        "post_content": "If police were trained to connect people to these hotlines, we wouldn't have as many issues as we do...",
        "post_title": "Philadelphia, Pennsylvania",
        "post_state": "Pennsylvania",
        "post_city": "",
    },
    {
        "post_content": "I want to make self-care a daily ritual but i don't know where to start.",
        "post_title": "Newport, Rhode Island",
        "post_state": "Rhode Island",
        "post_city": "",
    },
    {
        "post_content": "Not to get political, but homelessness shouldn't exist when we have billionaires.",
        "post_title": "Charleston, South Carolina",
        "post_state": "South Carolina",
        "post_city": "",
    },
    {
        "post_content": "If you haven't already, check out the stigma podcast. It's really good.",
        "post_title": "Sioux Falls, South Dakota",
        "post_state": "South Dakota",
        "post_city": "",
    },
    {
        "post_content": "All of my friends are starting to get facial hair and I still look like a kid. It is so embarrassing.",
        "post_title": "Nashville, Tennessee",
        "post_state": "Tennessee",
        "post_city": "",
    },
    {
        "post_content": "Still about #BLACKLIVESMATTER",
        "post_title": "Dallas, Texas",
        "post_state": "Texas",
        "post_city": "",
    },
    {
        "post_content": "I recently stopped drinking and I still feel a lot of shame. Anyone have any tips on how to feel better?",
        "post_title": "Moab, Utah",
        "post_state": "Utah",
        "post_city": "",
    },
    {
        "post_content": " I think I am addicted to porn, but i don't know. I don't know who else to tell so I figured i would post here.",
        "post_title": "Stowe, Vermont",
        "post_state": "Vermont",
        "post_city": "",
    },
    {
        "post_content": " My older sister has an eating disorder and I don't want to have one too. Is there anything I can do?",
        "post_title": "Richmond, Virginia",
        "post_state": "Virginia",
        "post_city": "",
    },
    {
        "post_content": "My ADHD makes it really hard to do well in school and it gives me a lot of anxiety because i want to go to a good college.",
        "post_title": "Seattle, Washington",
        "post_state": "Washington",
        "post_city": "",
    },
    {
        "post_content": "You are loved!!! I am there for you!",
        "post_title": "Morgantown, West Virginia",
        "post_state": "West Virginia",
        "post_city": "",
    },
    {
        "post_content": " What are the best mental health resources for someone without insurance?",
        "post_title": "Madison, Wisconsin",
        "post_state": "Wisconsin",
        "post_city": "",
    },
    {
        "post_content": "What should I do if i'm worried about a friend of mine?",
        "post_title": "Jackson, Wyoming",
        "post_state": "Wyoming",
        "post_city": "",
    },
]

abbr = {
    "Alabama": "AL",
    "Alaska": "AK",
    "American Samoa": "AS",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "District Of Columbia": "DC",
    "Federated States Of Micronesia": "FM",
    "Florida": "FL",
    "Georgia": "GA",
    "Guam": "GU",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Marshall Islands": "MH",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Northern Mariana Islands": "MP",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Palau": "PW",
    "Pennsylvania": "PA",
    "Puerto Rico": "PR",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virgin Islands": "VI",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    result= start_date + datetime.timedelta(days=random_number_of_days)
    return result
def createPost():
    for _ in range(0, len(users)):
        userData = users.pop()
        userData["profile_pic"]= f"Avatar/{random.randrange(1,9)}.PNG"
        userData["full_name"] = userData["email"].split("@")[0]
        newUser = CustomUserModel.objects.create(**userData)
        postData = posts.pop()
        postData['post_city']=postData["post_title"].split(',')[0]
        postData[
            "post_title"
        ] = f"{postData['post_title'].split(',')[0]}, {abbr[postData['post_state']]}"
        postData["user"] = newUser
        start_date = datetime.date(2021, 3, 14)
        end_date = datetime.date(2021, 3, 18)
        postData['post_content']=f"<p>{postData['post_content']}</p>"
        newPost=Post.objects.create(**postData)
        newPost.created_at=random_date(start_date,end_date)
        newPost.updated_at=random_date(start_date,end_date)
        newPost.save()

# from api.user.fakeDB import createPost
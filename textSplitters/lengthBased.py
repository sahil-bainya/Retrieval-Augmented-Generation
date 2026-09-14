from langchain_text_splitters import CharacterTextSplitter

text = """
Essay on Cricket
Cricket is one of the most popular sports in the world, especially in countries such as India, Australia, England, Pakistan, South Africa, and New Zealand. It is a team sport that combines skill, strategy, concentration, and physical fitness. For millions of people, cricket is not just a game but an important part of their culture and everyday life.
Cricket is played between two teams, with eleven players on each side. The game is played on a large field with a rectangular pitch in the center. The main objective is to score more runs than the opposing team. One team bats while the other team bowls and fields. The batsmen try to score runs by hitting the ball, while the bowlers and fielders attempt to restrict the scoring and dismiss the batsmen.
There are different formats of cricket. Test cricket is the longest and most traditional format, with matches lasting up to five days. One-Day Internationals (ODIs) generally consist of 50 overs per side and provide a balance between traditional and limited-overs cricket. Twenty20 (T20) cricket is the shortest international format, with each team playing 20 overs. T20 has become extremely popular because of its fast pace, entertainment, and exciting finishes.
Cricket requires both individual talent and teamwork. A successful player needs discipline, patience, physical fitness, and the ability to remain calm under pressure. Batsmen need excellent hand-eye coordination, bowlers require accuracy and variations, and fielders need agility and quick reflexes. At the same time, players must work together and follow the team's strategy.
In India, cricket has a special place in people's hearts. The sport has produced many legendary players, including Sachin Tendulkar, Kapil Dev, Rahul Dravid, Anil Kumble, M. S. Dhoni, and Virat Kohli. India's victories in major international tournaments have created unforgettable moments for cricket fans. The Indian Premier League (IPL) has also contributed significantly to the popularity and growth of T20 cricket.
Cricket also teaches valuable lessons beyond the playing field. It teaches us the importance of teamwork, perseverance, sportsmanship, leadership, and accepting both victory and defeat. A player may fail in one match but can learn from mistakes and perform better in the next. This makes cricket a sport that develops not only physical abilities but also mental strength.
However, cricket should be played and followed in the spirit of sportsmanship. Winning is important, but respecting opponents, officials, and teammates is equally valuable. Young people should also balance their interest in cricket with education, health, and other responsibilities.
In conclusion, cricket is much more than a game. It brings people together, creates memorable moments, encourages healthy competition, and teaches important values. Its combination of skill, strategy, teamwork, and excitement has made it one of the world's most loved sports. For millions of fans, cricket will continue to be a source of passion, inspiration, and entertainment for generations to come.
"""
splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator="")

result = splitter.split_text(text)

for t in result:
    print(t)
    print('---------------------------------')

-- sqlite3 weblog.sqlite3 < 20200224T184900-insert_posts_and_comments.sql

-- text from http://shakespeare.mit.edu/tempest/full.html

insert into posts (id, slug, title, body) values (
  1,
  "act_1_scene_1",
  "On a ship at sea: a tempestuous noise",
  "Enter a Master and a Boatswain"
);

insert into comments (post_id, author, body) values (
  1, "Master", "Boatswain!"
);

insert into comments (post_id, author, body) values (
  1, "Boatswain", "Here, master: what cheer?"
);

insert into comments (post_id, author, body) values (
  1, "Master", "Good, speak to the mariners nfall to't, yarely,
or we run ourselves aground: bestir, bestir."
);

insert into comments (post_id, author, body) values (
  1, "Boatswain", "Heigh, my hearts! cheerly, cheerly, my hearts!
yare, yare! Take in the topsail. Tend to the
master's whistle. Blow, till thou burst thy wind,
if room enough!"
);

insert into posts (id, slug, title, body) values (
  2,
  "act_1_scene_2",
  "The island. Before PROSPERO'S cell.",
  "If by your art, my dearest father, you have
Put the wild waters in this roar, allay them.
The sky, it seems, would pour down stinking pitch,
But that the sea, mounting to the welkin's cheek,
Dashes the fire out. O, I have suffered
With those that I saw suffer: a brave vessel,
Who had, no doubt, some noble creature in her,
Dash'd all to pieces. O, the cry did knock
Against my very heart. Poor souls, they perish'd.
Had I been any god of power, I would
Have sunk the sea within the earth or ere
It should the good ship so have swallow'd and
The fraughting souls within her."
);

insert into comments (post_id, author, body) values (
  2, "Prospero", "Be collected:
No more amazement: tell your piteous heart
There's no harm done."
);

insert into comments (post_id, author, body) values (
  2, "Miranda", "O, woe the day!"
);

insert into posts (id, slug, title, body) values (
  3,
  "act_2_scene_1",
  "Another part of the island.",
  "Beseech you, sir, be merry; you have cause,
So have we all, of joy; for our escape
Is much beyond our loss. Our hint of woe
Is common; every day some sailor's wife,
The masters of some merchant and the merchant
Have just our theme of woe; but for the miracle,
I mean our preservation, few in millions
Can speak like us: then wisely, good sir, weigh
Our sorrow with our comfort."
);

insert into comments (post_id, author, body) values (
  3, "Alonso", "Prithee, peace."
);

insert into comments (post_id, author, body) values (
  3, "Sebastian", "He receives comfort like cold porridge."
);

insert into comments (post_id, author, body) values (
  3, "Alonso", "The visitor will not give him o'er so."
);

insert into comments (post_id, author, body) values (
  3, "Sebastian", "Look he's winding up the watch of his wit;
by and by it will strike."
);

insert into posts (id, slug, title, body) values (
  4,
  "act_2_scene_2",
  "Another part of the island.",
  "All the infections that the sun sucks up
From bogs, fens, flats, on Prosper fall and make him
By inch-meal a disease! His spirits hear me
And yet I needs must curse. But they'll nor pinch,
Fright me with urchin--shows, pitch me i' the mire,
Nor lead me, like a firebrand, in the dark
Out of my way, unless he bid 'em; but
For every trifle are they set upon me;
Sometime like apes that mow and chatter at me
And after bite me, then like hedgehogs which
Lie tumbling in my barefoot way and mount
Their pricks at my footfall; sometime am I
All wound with adders who with cloven tongues
Do hiss me into madness.

Enter TRINCULO

Lo, now, lo!
Here comes a spirit of his, and to torment me
For bringing wood in slowly. I'll fall flat;
Perchance he will not mind me."
);

insert into comments (post_id, author, body) values (
  4, "Trinculo", "Here's neither bush nor shrub, to bear off
any weather at all, and another storm brewing;
I hear it sing i' the wind: yond same black
cloud, yond huge one, looks like a foul
bombard that would shed his liquor. If it
should thunder as it did before, I know not
where to hide my head: yond same cloud cannot
choose but fall by pailfuls. What have we
here? a man or a fish? dead or alive? A fish:
he smells like a fish; a very ancient and fish-
like smell; a kind of not of the newest Poor-
John. A strange fish! Were I in England now,
as once I was, and had but this fish painted,
not a holiday fool there but would give a piece
of silver: there would this monster make a
man; any strange beast there makes a man:
when they will not give a doit to relieve a lame
beggar, they will lazy out ten to see a dead
Indian. Legged like a man and his fins like
arms! Warm o' my troth! I do now let loose
my opinion; hold it no longer: this is no fish,
but an islander, that hath lately suffered by a
thunderbolt.

Thunder

Alas, the storm is come again! my best way is to
creep under his gaberdine; there is no other
shelter hereabouts: misery acquaints a man with
strange bed-fellows. I will here shroud till the
dregs of the storm be past.

Enter STEPHANO, singing: a bottle in his hand"
);

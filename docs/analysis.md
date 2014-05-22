# Analyzing Dota 2 Game Results

## Observations

Observations are merely facts about the data set.

Examples of Observations

>- Total Matches
>- Total Matches of Game Type
>- Number of Played Heroes
>- Number of Purchased Items
>- Number of Wins
>- Total Gold Spent
>- Total Damage Done
>- Total Tower Damage Done
>- Total Healing
>- Total K/D/A
>- Total LH/D

## Team Dependent Tests (??)

These tests are game wide, meaning one result per game. The results for one
team depend on the other team in the game, and will oppose those results.

This can be considered game wide:

Hypotheses will take the form:

>- Team has more last_hits
>- Team has more gold spent
>- Team has more healing

## Team Independent Tests

These tests are team wide, meaning each game has two results. The results from
one team does not depend on the other.

### Radiant Vs Dire

Hypothesis is team is radiant.

Could Indicate Map Advantages

### Number of Non-Private Accounts

Hypothesis is team contains greater than or equal than num non-private accounts

    NPAccountTest(team, num)

Could possibly indicate that players committed enough to share statistics
(presumably to follow DotaBuff etc.) are higher skilled.

### Hero Influence

Hypothesis is team contains [1-5] hero id's

    MultiHeroIDTest(team, ids[])

Examples of Possible Hypotheses

>- Hero Combinations
>- Str, Int, Agi Combos
>- Melee Vs Ranged Combos

### Item Influence

Hypothesis is team contains item id greater than or equal to num times

    ItemTest(team, i_id, num=1)

Examples of Possible Hypotheses

>- Magic Stick Winrate Across the Team
>- More Rapiers
>- Multiple Vlads
>- Wards/Smokes/Tps


## Limitations

### Poor API

The Dota 2 API has the limitation of only reporting the state of the game
as it ended. This means that nothing about the progression of the game gets
recorded, with the exception of ability leveling order.

The immediate issue that comes from this is item accuracy. We cannot tell
anything about what items were built and sold before the final game state.
Possible further analysis can come from the 'Gold Spent' field.

This also has the effect of ignoring what phase the game is in when it is won.
Game duration is something that should be taken into account for an accurate
and meaningful hypothesis when considering items.

### Skill Levels

The API reports games in three tiers of skill level. The variance in the
validity of the data from each tier is staggering. The algorithm to throw out
'trash' games (games shorter than 10 min, games with leavers etc) filters out
90% of the low tier games, and only 20-50% for the high and very high tiers.
Discrepancies are assumed to be present in all other fields between the three
tiers.

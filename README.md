SnapeRobot.py is the brains of the robot.  It looks for comments containing the triggers, builds responses to those triggers, and posts a reply if it hasn't already replied.

triggers.xml contains the triggers.  For each trigger, create a new "comment" element and fill in the "trigger" and "response" attributes.
Be careful not to have triggers that are subsets of others.  For example, a trigger of "James Potter" and another trigger of "Potter" will result in both triggers being used when "James Potter" is in the comment.
import random
import string
import time


class MonkeyTypewriter(object):
    def __init__(self, upper=True, spaces=True, punctuation=True):

        self.works = {
            'Sonnet1': "From fairest creatures we desire increase, That thereby beauty's rose might never die, But as the riper should by time decease, His tender heir might bear his memory: But thou, contracted to thine own bright eyes, Feed'st thy light'st flame with self-substantial fuel, Making a famine where abundance lies, Thyself thy foe, to thy sweet self too cruel. Thou that art now the world's fresh ornament And only herald to the gaudy spring, Within thine own bud buriest thy content And, tender churl, makest waste in niggarding. Pity the world, or else this glutton be, To eat the world's due, by the grave and thee.",
            'Sonnet2': "When forty winters shall beseige thy brow, And dig deep trenches in thy beauty's field, Thy youth's proud livery, so gazed on now, Will be a tatter'd weed, of small worth held: Then being ask'd where all thy beauty lies, Where all the treasure of thy lusty days, To say, within thine own deep-sunken eyes, Were an all-eating shame and thriftless praise. How much more praise deserved thy beauty's use, If thou couldst answer 'This fair child of mine Shall sum my count and make my old excuse,' Proving his beauty by succession thine! This were to be new made when thou art old, And see thy blood warm when thou feel'st it cold.",
            'Sonnet3': "Look in thy glass, and tell the face thou viewest Now is the time that face should form another; Whose fresh repair if now thou not renewest, Thou dost beguile the world, unbless some mother. For where is she so fair whose unear'd womb Disdains the tillage of thy husbandry? Or who is he so fond will be the tomb Of his self-love, to stop posterity? Thou art thy mother's glass, and she in thee Calls back the lovely April of her prime: So thou through windows of thine age shall see Despite of wrinkles this thy golden time. But if thou live, remember'd not to be, Die single, and thine image dies with thee.",
            'Sonnet4': "Unthrifty loveliness, why dost thou spend Upon thyself thy beauty's legacy? Nature's bequest gives nothing but doth lend, And being frank she lends to those are free. Then, beauteous niggard, why dost thou abuse The bounteous largess given thee to give? Profitless usurer, why dost thou use So great a sum of sums, yet canst not live? For having traffic with thyself alone, Thou of thyself thy sweet self dost deceive. Then how, when nature calls thee to be gone, What acceptable audit canst thou leave? Thy unused beauty must be tomb'd with thee, Which, used, lives th' executor to be.",
            'Sonnet5': "Those hours, that with gentle work did frame The lovely gaze where every eye doth dwell, Will play the tyrants to the very same And that unfair which fairly doth excel: For never-resting time leads summer on To hideous winter and confounds him there; Sap cheque'd with frost and lusty leaves quite gone, Beauty o'ersnow'd and bareness every where: Then, were not summer's distillation left, A liquid prisoner pent in walls of glass, Beauty's effect with beauty were bereft, Nor it nor no remembrance what it was: But flowers distill'd though they with winter meet, Leese but their show; their substance still lives sweet.",
            'Sonnet6': "Then let not winter's ragged hand deface In thee thy summer, ere thou be distill'd: Make sweet some vial; treasure thou some place With beauty's treasure, ere it be self-kill'd. That use is not forbidden usury, 5 Which happies those that pay the willing loan; That's for thyself to breed another thee, Or ten times happier, be it ten for one; Ten times thyself were happier than thou art, If ten of thine ten times refigured thee: 10 Then what could death do, if thou shouldst depart, Leaving thee living in posterity? Be not self-will'd, for thou art much too fair To be death's conquest and make worms thine heir."
        }
        self.start_seconds = time.time()
        self.punctuation_chars = '.,?!\'";:-'

        self.char_set = string.lowercase
        if upper:
            self.char_set += string.uppercase
        if spaces:
            self.char_set += ' '
        if punctuation:
            self.char_set += self.punctuation_chars

        for work, text in self.works.items():
            if not upper:
                text = text.lower()
            if not spaces:
                text = text.replace(' ', '')
            if not punctuation:
                for char in self.punctuation_chars:
                    text = text.replace(char, '')
            self.works[work] = text

    def random_char(self):
        """
        Get a random character from possible chars
        :return:
        """
        return random.choice(self.char_set)

    def any_work_in_progress(self, monkey_wip_text):
        """
        Check if any work is still accurate

        :param monkey_wip_text:
        :return:
        """
        for work, text in self.works.items():
            if text.startswith(monkey_wip_text):
                return True

    def get_time_text(self, seconds):
        """
        Get time string from seconds formated "{}h {}m {}s"

        :param seconds:
        :return:
        """
        return '{}h {}m {}s'.format(
            int(seconds / 3600),
            int(seconds / 60) % 60,
            int(seconds) % 60
        )

    def monkey_type(self):
        """
        Get that monkey typing

        :return:
        """
        monkey_wip_text = ''
        best_text = ''

        while True:
            monkey_wip_text += self.random_char()
            if not self.any_work_in_progress(monkey_wip_text):
                if len(monkey_wip_text) > len(best_text):
                    end_seconds = time.time()
                    time_difference_text = self.get_time_text(
                        end_seconds - self.start_seconds
                    )
                    print 'New best after {}: "{}"'.format(
                        time_difference_text, monkey_wip_text
                    )
                    best_text = monkey_wip_text
                monkey_wip_text = ''

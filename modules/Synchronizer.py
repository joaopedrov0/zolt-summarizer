# Main class

class VoiceStack:
    # Pilha de {start, stop, speaker}
    def __init__(self):
        self.stack = []
        
    def get(self):
        if len(self.stack) == 0:
            return
        return self.stack[len(self.stack) - 1]
    
    def clear_dead_speakers(self, time):
        cleaned_list = [
            speaker for speaker in self.stack
            if speaker["stop"] > time
        ]
        print("Cleaned list: ", cleaned_list)
        self.stack = cleaned_list
        
    def append(self, speaker, start, stop):
        # print("Appending speaker:", speaker, "start:", start, "stop:", stop)
        self.stack.append({
            "speaker": speaker,
            "start": start,
            "stop": stop
        })
        
class Synchronizer:
    
    
    @staticmethod
    def sync(transcription_segments, speakers_dictionary):
        """
        Docstring for sync
        
        :param transcription_segments: list(dict(text, start, stop))
        :param speakers_dictionary: list(dict(speaker, start, stop))
        """
        
        res = {}
        
        
        vs = VoiceStack()
        vs.append(
            speakers_dictionary[0]["speaker"],
            speakers_dictionary[0]["start"],
            speakers_dictionary[0]["stop"]
            )
        del speakers_dictionary[0]
        
        time = vs.get()["start"]
        
        while(len(transcription_segments) > 0):
            # print("CURRENT RES: ", len(res))
            # print("TIME: ", time)
            # limpa speakers inativos
            # vs.clear_dead_speakers(time)
            
            # register transcription segment with speaker
            res[f"{transcription_segments[0]["start"]:.2f} - {transcription_segments[0]["stop"]:.2f}"] = {
                "speaker": vs.get()["speaker"],
                "text": transcription_segments[0]["text"]
            }
            # print("speaker: ", vs.get()["speaker"])
            # print("text: ", transcription_segments[0]["text"])
            
            # if a new speaker start speaking, he's appended on stack
            if len(speakers_dictionary) > 0:
                if float(time) >= float(speakers_dictionary[0]["start"]):
                    vs.append(
                        speakers_dictionary[0]["speaker"],
                        speakers_dictionary[0]["start"],
                        speakers_dictionary[0]["stop"]
                        )
                    del speakers_dictionary[0]
            
            # remove current transcription segment
            del transcription_segments[0]
            
            # updates time with the next transcription segment
            if len(transcription_segments) > 0:
                time = transcription_segments[0]["start"]
            
            # print("\n\n\n")
            
        return res
            
        
    
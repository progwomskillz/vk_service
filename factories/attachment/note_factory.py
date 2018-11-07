from vk_service.models.attachment.note import Note


class NoteFactory:
    def build(self, values):
        return Note(values)

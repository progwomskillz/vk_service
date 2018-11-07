from vk_service.models.attachment import Note


class NoteFactory:
    def build(self, values):
        return Note(values)

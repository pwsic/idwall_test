from sqlalchemy import select


class BaseRepository:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def get_by_id(self, id):
        query = select(self.model).where(self.model.id == id)
        result = self.session.execute(query)
        return result.scalars().one_or_none()

    def create(self, model):
        self.session.add(model)
        self.session.commit()
        return model

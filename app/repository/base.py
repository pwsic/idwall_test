from sqlalchemy import select, update


class BaseRepository:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def get_by_id(self, id_):
        query = select(self.model).where(self.model.id == id_)
        result = self.session.execute(query)
        return result.scalars().one_or_none()

    def create(self, model):
        self.session.add(model)
        self.session.commit()
        return model

    def update(self, data, id_):

        stmt = update(self.model).where(self.model.id == id_).values(**data)

        self.session.execute(stmt)
        return self.session.commit()

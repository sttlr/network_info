#!/usr/bin/env python3
# -*- coding: utf-8 -*- ®

from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy import literal_column
from db.helper import get_base
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import func

Base = get_base()


class Block(Base):
    __tablename__ = 'block'
    id = Column(Integer, primary_key=True)
    inetnum = Column(postgresql.CIDR, nullable=False, index=True)
    netname = Column(String, nullable=True, index=True)
    description = Column(String)
    source = Column(String, index=True)

    __table_args__ = (
        Index('ix_block_description', func.to_tsvector(literal_column("'english'"), description), postgresql_using="gin"), )

    def __str__(self):
        return f'inetnum: {self.inetnum}, netname: {self.netname}, description: {self.description}, source: {self.source}'

    def __repr__(self):
        return self.__str__()


class Organisation(Base):
    __tablename__ = 'organisation'
    id = Column(Integer, primary_key=True)
    organisation = Column(String, nullable=False, index=True)
    orgname = Column(String, nullable=True, index=True)
    source = Column(String, index=True)

    def __str__(self):
        return f'organisation: {self.organisation}, orgname: {self.orgname}, source: {self.source}'

    def __repr__(self):
        return self.__str__()


class ASN(Base):
    __tablename__ = 'asn'
    id = Column(Integer, primary_key=True)
    autnum = Column(String, nullable=False, index=True)
    asname = Column(String, nullable=True, index=True)
    description = Column(String)
    source = Column(String, index=True)

    __table_args__ = (
        Index('ix_asn_description', func.to_tsvector(literal_column("'english'"), description), postgresql_using="gin"), )

    def __str__(self):
        return f'autnum: {self.autnum}, asname: {self.asname}, description: {self.description}, source: {self.source}'

    def __repr__(self):
        return self.__str__()

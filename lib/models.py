from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from lib.database import Base
from typing import List, Optional

class Donor(Base):
    """
    Represents a donor in the blood donation system.
    """
    __tablename__ = 'donors'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    donations: Mapped[List["Donation"]] = relationship('Donation', back_populates='donor')

class Staff(Base):
    """
    Represents a staff member in the blood donation system.
    """
    __tablename__ = 'staff'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    donations: Mapped[List["Donation"]] = relationship('Donation', back_populates='staff')

class Donation(Base):
    """
    Represents a donation record linking a donor and staff.
    """
    __tablename__ = 'donations'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    donor_id: Mapped[int] = mapped_column(Integer, ForeignKey('donors.id'), nullable=False)
    staff_id: Mapped[int] = mapped_column(Integer, ForeignKey('staff.id'), nullable=False)

    donor: Mapped["Donor"] = relationship('Donor', back_populates='donations')
    staff: Mapped["Staff"] = relationship('Staff', back_populates='donations')
    tests: Mapped[List["Test"]] = relationship('Test', back_populates='donation')

class Test(Base):
    """
    Represents a test associated with a donation.
    """
    __tablename__ = 'tests'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    donation_id: Mapped[int] = mapped_column(Integer, ForeignKey('donations.id'), nullable=False)

    donation: Mapped["Donation"] = relationship('Donation', back_populates='tests')

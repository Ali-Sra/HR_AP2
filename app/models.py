from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    ForeignKey,
    Float,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base


# ---------- USER & HR ----------

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    authent_user_uuid = Column(String, unique=True, nullable=True)
    name = Column(String, nullable=False)
    family_name = Column(String, nullable=False)
    birthdate = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    entry_date = Column(Date, nullable=True)
    exit_date = Column(Date, nullable=True)
    status = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # روابط
    address = relationship("Address", back_populates="user", uselist=False)
    contracts = relationship("Contract", back_populates="user", cascade="all, delete-orphan")
    certificates = relationship("Certificate", back_populates="user", cascade="all, delete-orphan")
    reservations = relationship("Reservation", back_populates="user", cascade="all, delete-orphan")
    user_insurances = relationship("UserInsurance", back_populates="user", cascade="all, delete-orphan")
    languages = relationship("UserLanguage", back_populates="user", cascade="all, delete-orphan")
    groups = relationship("UserGroup", back_populates="user", cascade="all, delete-orphan")


class Address(Base):
    __tablename__ = "addresses"

    address_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    street = Column(String, nullable=True)
    house_number = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    postal_code = Column(String, nullable=True)
    city = Column(String, nullable=True)
    mobile_number = Column(String, nullable=True)

    user = relationship("User", back_populates="address")


class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    contracts = relationship("Contract", back_populates="department")


class Position(Base):
    __tablename__ = "positions"

    position_id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=True)
    salary_range = Column(String, nullable=True)
    title = Column(String, nullable=False, unique=True)

    contracts = relationship("Contract", back_populates="position")


class WorkingTimeType(Base):
    __tablename__ = "working_time_types"

    working_time_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)

    contracts = relationship("Contract", back_populates="working_time_type")


class Contract(Base):
    __tablename__ = "contracts"

    contract_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    working_time_type_id = Column(Integer, ForeignKey("working_time_types.working_time_type_id"))
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    position_id = Column(Integer, ForeignKey("positions.position_id"))

    base_salary = Column(Float, nullable=True)
    contract_type = Column(String, nullable=True)
    start_at = Column(Date, nullable=True)
    end_at = Column(Date, nullable=True)
    status = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="contracts")
    department = relationship("Department", back_populates="contracts")
    position = relationship("Position", back_populates="contracts")
    working_time_type = relationship("WorkingTimeType", back_populates="contracts")
    salaries = relationship("Salary", back_populates="contract", cascade="all, delete-orphan")


class Salary(Base):
    __tablename__ = "salaries"

    salary_id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.contract_id"), nullable=False)
    base_salary = Column(Float, nullable=False)
    valid_from = Column(Date, nullable=False)
    valid_until = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    contract = relationship("Contract", back_populates="salaries")


class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    certificate_type = Column(String, nullable=False)
    certificate_number = Column(String, nullable=True)
    issued_at = Column(Date, nullable=True)
    valid_until = Column(Date, nullable=True)
    next_verification_at = Column(Date, nullable=True)
    status = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="certificates")


# ---------- LANGUAGE & GROUP (n:m) ----------

class Language(Base):
    __tablename__ = "languages"

    language_id = Column(Integer, primary_key=True, index=True)
    iso_code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_languages = relationship("UserLanguage", back_populates="language")


class UserLanguage(Base):
    __tablename__ = "user_languages"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    language_id = Column(Integer, ForeignKey("languages.language_id"), primary_key=True)

    proficiency_level = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="languages")
    language = relationship("Language", back_populates="user_languages")


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    status = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_groups = relationship("UserGroup", back_populates="group")


class UserGroup(Base):
    __tablename__ = "user_groups"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.group_id"), primary_key=True)

    from_date = Column(Date, nullable=True)
    to_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="groups")
    group = relationship("Group", back_populates="user_groups")


# ---------- RESOURCES / RESERVATIONS ----------

class Resource(Base):
    __tablename__ = "resources"

    resource_id = Column(Integer, primary_key=True, index=True)
    resource_type = Column(String, nullable=False)  # e.g. 'room', 'car', 'device'
    display_name = Column(String, nullable=False)
    status = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    reservations = relationship("Reservation", back_populates="resource", cascade="all, delete-orphan")
    room = relationship("Room", back_populates="resource", uselist=False, cascade="all, delete-orphan")
    car = relationship("Car", back_populates="resource", uselist=False, cascade="all, delete-orphan")


class Room(Base):
    __tablename__ = "rooms"

    room_id = Column(Integer, ForeignKey("resources.resource_id"), primary_key=True)
    room_name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=True)
    status = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    description = Column(String, nullable=True)

    resource = relationship("Resource", back_populates="room")


class Car(Base):
    __tablename__ = "cars"

    car_id = Column(Integer, ForeignKey("resources.resource_id"), primary_key=True)
    license_plate = Column(String, nullable=False, unique=True)
    brand = Column(String, nullable=True)
    model = Column(String, nullable=True)
    year_of_construction = Column(Integer, nullable=True)
    state = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    resource = relationship("Resource", back_populates="car")


class Reservation(Base):
    __tablename__ = "reservations"

    reservation_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    resource_id = Column(Integer, ForeignKey("resources.resource_id"), nullable=False)

    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=False)
    status = Column(String, nullable=True)
    purpose = Column(String, nullable=True)
    created_by = Column(Integer, nullable=True)
    cancelled_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="reservations")
    resource = relationship("Resource", back_populates="reservations")


# ---------- INSURANCE ----------

class InsuranceType(Base):
    __tablename__ = "insurance_types"

    insurance_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)

    user_insurances = relationship("UserInsurance", back_populates="insurance_type")


class UserInsurance(Base):
    __tablename__ = "user_insurances"

    insurance_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    insurance_type_id = Column(Integer, ForeignKey("insurance_types.insurance_type_id"), nullable=False)

    provider = Column(String, nullable=True)
    insurance_number = Column(String, nullable=True)
    start_at = Column(Date, nullable=True)
    status = Column(String, nullable=True)

    user = relationship("User", back_populates="user_insurances")
    insurance_type = relationship("InsuranceType", back_populates="user_insurances")


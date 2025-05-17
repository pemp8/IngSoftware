# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Agendamiento(models.Model):
      # Guarda citas médicas con datos de profesional, paciente, especialidad y estado.
    cod_m = models.ForeignKey(
        'Profesional',
        db_column='cod_m',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    esp_m = models.ForeignKey(
        'Especialidad',
        db_column='esp_m',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.CharField(max_length=5, blank=True, null=True)
    ficha = models.IntegerField(blank=True, null=True)
    vino = models.IntegerField(blank=True, null=True)
    atendio = models.IntegerField(blank=True, null=True)
    observa = models.CharField(max_length=150, blank=True, null=True)
    fonasa = models.IntegerField(blank=True, null=True)
    hora_llegada = models.CharField(max_length=50, blank=True, null=True)
    lugar_aten = models.CharField(max_length=50, blank=True, null=True)
    rut = models.IntegerField(blank=True, null=True)
    dv = models.CharField(max_length=1, blank=True, null=True)
    idpaciente = models.ForeignKey(
        'Paciente',
        db_column='idPaciente',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    medico = models.CharField(max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)
    especialidad = models.CharField(max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)
    pervision = models.CharField(max_length=50, blank=True, null=True)
    fec_naci = models.DateTimeField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    preparado = models.IntegerField(blank=True, null=True)
    sincronizado = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    correlativo = models.BigIntegerField(unique=True, blank=True, null=True)
    llamo = models.CharField(max_length=1, blank=True, null=True)
    sv = models.CharField(max_length=1, blank=True, null=True)
    ges = models.IntegerField(blank=True, null=True)
    prais = models.IntegerField(blank=True, null=True)
    vinodate = models.DateTimeField(db_column='vinoDate', blank=True, null=True)  # Field name made lowercase.
    pagodate = models.DateTimeField(db_column='pagoDate', blank=True, null=True)  # Field name made lowercase.
    llamodate = models.DateTimeField(db_column='llamoDate', blank=True, null=True)  # Field name made lowercase.
    sexo = models.SmallIntegerField(blank=True, null=True)
    nom_pa = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ape_pater_pa = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ape_mater_pa = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    nom_med = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ape_pater_med = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    ape_mater_med = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    rut_medico = models.BigIntegerField(blank=True, null=True)
    dv_medico = models.CharField(max_length=1, blank=True, null=True)
    oracle_cit_corr = models.BigIntegerField(blank=True, null=True)
    oracle_traspasado = models.CharField(max_length=2, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agendamiento'


class Especialidad(models.Model):
        # Lista de especialidades médicas.
    idespecialidad = models.AutoField(primary_key=True)
    especialidad = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidad'


class Box(models.Model):
        # Representa salas/unidades asociadas a una especialidad.
    idbox = models.IntegerField(primary_key=True)
    idEspecialidad = models.ForeignKey(
        Especialidad,
        db_column='idEspecialidad',
        on_delete=models.DO_NOTHING,
        blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = 'box'


class Profesional(models.Model):
        # Datos básicos de profesionales de salud y su especialidad.
    idprofesional = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    idespecialidad = models.ForeignKey(
        Especialidad, 
        models.DO_NOTHING, 
        db_column='idEspecialidad', 
        blank=True, null=True
    )  # Field name made lowercase.
    fechanacimiento = models.DateTimeField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    rut = models.IntegerField(blank=True, null=True)
    dv = models.CharField(max_length=1, blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesional'


class Paciente(models.Model):
        # Información básica de pacientes.
    idpaciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    pacientecol = models.CharField(max_length=45, blank=True, null=True)
    fechanacimiento = models.DateTimeField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    rut = models.IntegerField(blank=True, null=True)
    dv = models.CharField(max_length=1, blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)
    fonasa = models.IntegerField(blank=True, null=True)
    pervision = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class Mantenimiento(models.Model):
        # Marca períodos en que un box está en mantenimiento.
    idmantenimiento = models.AutoField(primary_key=True)
    idbox = models.ForeignKey(
        Box, 
        models.DO_NOTHING, 
        db_column='idBox', 
        blank=True, null=True
    )  # Field name made lowercase.
    inicio = models.DateTimeField(blank=True, null=True)
    termino = models.DateTimeField(blank=True, null=True)
    motivo = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mantenimiento'

class Asignacion(models.Model):
        # Asocia un agendamiento a un box con fecha de asignación.
    idasignacion = models.AutoField(primary_key=True)
    idAgendamiento = models.ForeignKey(
        'Agendamiento',
        db_column='idAgendamiento',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    idBox = models.ForeignKey(
        'Box',
        db_column='idBox',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    fechaCreacion = models.DateTimeField(
        db_column='fechaCreacion',
        auto_now_add=True
    )

    class Meta:
        managed = False
        db_table = 'asignacion'


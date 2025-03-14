from rest_framework import serializers

class ClimaSerializer(serializers.Serializer):
    cidade = serializers.CharField()
    temperatura = serializers.CharField()
    sensacao_termica = serializers.CharField()
    umidade = serializers.CharField()
    descricao = serializers.CharField()

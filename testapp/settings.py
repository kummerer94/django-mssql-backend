import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite'),
    'other': dj_database_url.config(env='DATABASE_URL_OTHER', default='sqlite:///db.sqlite'),
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'sql_server.pyodbc',
    'testapp',
)


TEST_RUNNER = 'testapp.runner.ExcludeTestSuiteRunner'
EXCLUDED_TESTS = (
    'aggregation.tests.AggregateTestCase.test_aggregation_subquery_annotation_exists',
    'aggregation.tests.AggregateTestCase.test_aggregation_subquery_annotation_values_collision',
    'aggregation.tests.AggregateTestCase.test_count_star',
    'aggregation.tests.AggregateTestCase.test_distinct_on_aggregate',
    'aggregation.tests.AggregateTestCase.test_expression_on_aggregation',
    'aggregation_regress.tests.AggregationTests.test_annotated_conditional_aggregate',
    'aggregation_regress.tests.AggregationTests.test_annotation_with_value',
    'aggregation_regress.tests.AggregationTests.test_more_more',
    'aggregation_regress.tests.AggregationTests.test_more_more_more',
    'aggregation_regress.tests.AggregationTests.test_ticket_11293',
    'aggregation_regress.tests.AggregationTests.test_values_list_annotation_args_ordering',
    'annotations.tests.NonAggregateAnnotationTestCase.test_annotate_exists',
    'annotations.tests.NonAggregateAnnotationTestCase.test_combined_expression_annotation_with_aggregation',
    'backends.tests.BackendTestCase.test_queries',
    'backends.tests.BackendTestCase.test_unicode_password',
    'backends.tests.FkConstraintsTests.test_disable_constraint_checks_context_manager',
    'backends.tests.FkConstraintsTests.test_disable_constraint_checks_manually',
    'backends.tests.LastExecutedQueryTest.test_last_executed_query',
    'bulk_create.tests.BulkCreateTests.test_bulk_insert_nullable_fields',
    'constraints.tests.CheckConstraintTests.test_abstract_name',
    'constraints.tests.CheckConstraintTests.test_database_constraint',
    'constraints.tests.CheckConstraintTests.test_database_constraint_expression',
    'constraints.tests.CheckConstraintTests.test_database_constraint_expressionwrapper',
    'constraints.tests.CheckConstraintTests.test_name',
    'constraints.tests.UniqueConstraintTests.test_database_constraint',
    'constraints.tests.UniqueConstraintTests.test_database_constraint_with_condition',
    'constraints.tests.UniqueConstraintTests.test_name',
    'custom_lookups.tests.BilateralTransformTests.test_transform_order_by',
    'datatypes.tests.DataTypesTestCase.test_error_on_timezone',
    'datetimes.tests.DateTimesTests.test_datetimes_ambiguous_and_invalid_times',
    'datetimes.tests.DateTimesTests.test_datetimes_returns_available_dates_for_given_scope_and_given_field',
    'datetimes.tests.DateTimesTests.test_related_model_traverse',
    'db_functions.comparison.test_cast.CastTests.test_cast_to_integer',
    'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_extract_func',
    'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_extract_iso_weekday_func',
    'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_extract_year_exact_lookup',
    'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_extract_year_greaterthan_lookup',
    'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_extract_year_lessthan_lookup',
    'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_trunc_func',
    'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_trunc_week_func',
    'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_extract_func',
    'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_extract_func_with_timezone',
    'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_extract_iso_weekday_func',
    'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_extract_year_exact_lookup',
    'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_extract_year_greaterthan_lookup',
    'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_extract_year_lessthan_lookup',
    'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_trunc_ambiguous_and_invalid_times',
    'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_trunc_func_with_timezone',
    'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_trunc_none',
    'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_trunc_week_func',
    'db_functions.math.test_degrees.DegreesTests.test_integer',
    'db_functions.math.test_mod.ModTests.test_float',
    'db_functions.math.test_power.PowerTests.test_integer',
    'db_functions.math.test_radians.RadiansTests.test_integer',
    'db_functions.text.test_md5',
    'db_functions.text.test_pad.PadTests.test_pad',
    'db_functions.text.test_replace.ReplaceTests.test_case_sensitive',
    'db_functions.text.test_sha1',
    'db_functions.text.test_sha224',
    'db_functions.text.test_sha256',
    'db_functions.text.test_sha384',
    'db_functions.text.test_sha512',
    'dbshell.tests.DbshellCommandTestCase.test_command_missing',
    'defer_regress.tests.DeferRegressionTest.test_ticket_23270',
    'delete.tests.DeletionTests.test_only_referenced_fields_selected',
    'expressions.tests.BasicExpressionsTests.test_case_in_filter_if_boolean_output_field',
    'expressions.tests.BasicExpressionsTests.test_filtering_on_annotate_that_uses_q',
    'expressions.tests.BasicExpressionsTests.test_order_by_exists',
    'expressions.tests.BasicExpressionsTests.test_subquery_in_filter',
    'expressions.tests.ExpressionOperatorTests.test_lefthand_bitwise_right_shift_operator',
    'expressions.tests.ExpressionOperatorTests.test_lefthand_bitwise_xor',
    'expressions.tests.ExpressionOperatorTests.test_lefthand_bitwise_xor_null',
    'expressions.tests.ExpressionOperatorTests.test_righthand_power',
    'expressions.tests.FTimeDeltaTests.test_date_subquery_subtraction',
    'expressions.tests.FTimeDeltaTests.test_datetime_subquery_subtraction',
    'expressions.tests.FTimeDeltaTests.test_datetime_subtraction_microseconds',
    'expressions.tests.FTimeDeltaTests.test_duration_with_datetime_microseconds',
    'expressions.tests.FTimeDeltaTests.test_invalid_operator',
    'expressions.tests.FTimeDeltaTests.test_time_subquery_subtraction',
    'expressions.tests.IterableLookupInnerExpressionsTests.test_expressions_in_lookups_join_choice',
    'expressions_case.tests.CaseExpressionTests.test_annotate_with_in_clause',
    'fixtures_regress.tests.TestFixtures.test_loaddata_raises_error_when_fixture_has_invalid_foreign_key',
    'fixtures_regress.tests.TestFixtures.test_loaddata_with_m2m_to_self',
    'fixtures_regress.tests.TestFixtures.test_loaddata_with_valid_fixture_dirs',
    'fixtures_regress.tests.TestFixtures.test_loaddata_works_when_fixture_has_forward_refs',
    'fixtures_regress.tests.TestFixtures.test_path_containing_dots',
    'fixtures_regress.tests.TestFixtures.test_pg_sequence_resetting_checks',
    'fixtures_regress.tests.TestFixtures.test_pretty_print_xml',
    'fixtures_regress.tests.TestFixtures.test_proxy_model_included',
    'fixtures_regress.tests.TestFixtures.test_relative_path',
    'fixtures_regress.tests.TestFixtures.test_relative_path_in_fixture_dirs',
    'fixtures_regress.tests.TestFixtures.test_ticket_20820',
    'fixtures_regress.tests.TestFixtures.test_ticket_22421',
    'get_or_create.tests.UpdateOrCreateTransactionTests.test_creation_in_transaction',
    'indexes.tests.PartialIndexTests.test_multiple_conditions',
    'indexes.tests.SchemaIndexesNotPostgreSQLTests.test_create_index_ignores_opclasses',
    'inspectdb.tests.InspectDBTestCase.test_introspection_errors',
    'introspection.tests.IntrospectionTests.test_get_constraints',
    'introspection.tests.IntrospectionTests.test_get_table_description_types',
    'introspection.tests.IntrospectionTests.test_smallautofield',
    'invalid_models_tests.test_ordinary_fields.TextFieldTests.test_max_length_warning',
    'migrate_signals.tests.MigrateSignalTests.test_migrations_only',
    'model_fields.test_integerfield.PositiveBigIntegerFieldTests',
    'model_fields.test_jsonfield',
    'model_indexes.tests.IndexesTests.test_db_tablespace',
    'ordering.tests.OrderingTests.test_deprecated_values_annotate',
    'ordering.tests.OrderingTests.test_order_by_fk_attname',
    'ordering.tests.OrderingTests.test_order_by_pk',
    'ordering.tests.OrderingTests.test_orders_nulls_first_on_filtered_subquery',
    'prefetch_related.tests.GenericRelationTests.test_prefetch_GFK_nonint_pk',
    'queries.test_bulk_update.BulkUpdateNoteTests.test_set_field_to_null',
    'queries.test_bulk_update.BulkUpdateTests.test_json_field',
    'queries.test_db_returning',
    'queries.test_qs_combinators.QuerySetSetOperationTests.test_limits',
    'queries.test_qs_combinators.QuerySetSetOperationTests.test_ordering_by_f_expression_and_alias',
    'schema.tests.SchemaTests.test_add_foreign_key_quoted_db_table',
    'schema.tests.SchemaTests.test_alter_auto_field_quoted_db_column',
    'schema.tests.SchemaTests.test_alter_auto_field_to_char_field',
    'schema.tests.SchemaTests.test_alter_auto_field_to_integer_field',
    'schema.tests.SchemaTests.test_alter_autofield_pk_to_bigautofield_pk_sequence_owner',
    'schema.tests.SchemaTests.test_alter_autofield_pk_to_smallautofield_pk_sequence_owner',
    'schema.tests.SchemaTests.test_alter_implicit_id_to_explicit',
    'schema.tests.SchemaTests.test_alter_int_pk_to_autofield_pk',
    'schema.tests.SchemaTests.test_alter_int_pk_to_bigautofield_pk',
    'schema.tests.SchemaTests.test_alter_pk_with_self_referential_field',
    'schema.tests.SchemaTests.test_alter_primary_key_quoted_db_table',
    'schema.tests.SchemaTests.test_alter_smallint_pk_to_smallautofield_pk',
    'schema.tests.SchemaTests.test_char_field_pk_to_auto_field',
    'schema.tests.SchemaTests.test_inline_fk',
    'schema.tests.SchemaTests.test_no_db_constraint_added_during_primary_key_change',
    'schema.tests.SchemaTests.test_remove_field_check_does_not_remove_meta_constraints',
    'schema.tests.SchemaTests.test_remove_field_unique_does_not_remove_meta_constraints',
    'schema.tests.SchemaTests.test_remove_unique_together_does_not_remove_meta_constraints',
    'schema.tests.SchemaTests.test_text_field_with_db_index',
    'schema.tests.SchemaTests.test_unique_and_reverse_m2m',
    'schema.tests.SchemaTests.test_unique_no_unnecessary_fk_drops',
    'schema.tests.SchemaTests.test_unique_together_with_fk',
    'schema.tests.SchemaTests.test_unique_together_with_fk_with_existing_index',
    'select_for_update.tests.SelectForUpdateTests.test_for_update_after_from',
)

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
